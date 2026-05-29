from llvmlite import ir, binding

class CodeGen:
    def __init__(self):
        self.binding = binding
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()
        self._setup_module()
        self._create_execution_engine()
        self._declare_printf()
        self._print_counter = 0

    def _setup_module(self):
        self.module = ir.Module(name="lab13")
        self.module.triple = self.binding.get_default_triple()
        # Функция main не возвращает значения (void)
        func_type = ir.FunctionType(ir.VoidType(), [])
        self.main_func = ir.Function(self.module, func_type, name="main")
        block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def _create_execution_engine(self):
        target = self.binding.Target.from_default_triple()
        target_machine = target.create_target_machine()
        backing_mod = self.binding.parse_assembly("")
        self.engine = self.binding.create_mcjit_compiler(backing_mod, target_machine)

    def _declare_printf(self):
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

    def emit_print(self, value_llvm):
        """Генерирует вызов printf для целого числа"""
        self._print_counter += 1
        fmt = "%d\n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        fmt_name = f"fstr_{self._print_counter}"
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name=fmt_name)
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt

        voidptr_ty = ir.IntType(8).as_pointer()
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
        self.builder.call(self.printf, [fmt_arg, value_llvm])

    def finalize(self):
        """Завершает функцию main и компилирует модуль"""
        self.builder.ret_void()
        llvm_ir = str(self.module)
        mod = self.binding.parse_assembly(llvm_ir)
        mod.verify()
        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()

    def run(self):
        """Запускает скомпилированную функцию main"""
        func_ptr = self.engine.get_function_address("main")
        import ctypes
        cfunc = ctypes.CFUNCTYPE(None)(func_ptr)
        cfunc()

    def save_ir(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.module))
        print(f"LLVM IR сохранён в {filename}")