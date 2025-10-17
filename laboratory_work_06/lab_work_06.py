from math import sin, cos

def function_1(x):
    return (sin(2*x)+sin(5*x)-sin(3*x))/(cos(x)+1-2*sin(2*x)**2)

def function_2(x):
    return 2*sin(x)

with (open("input.txt", "r") as input_file):
    with open("output.txt", "w") as output_file:
        headr = "   x        y1          y2"
        print(headr)
        output_file.write(headr + "\n")
        for line in input_file:
            x_s = line.strip()
            if x_s:
                x = float(x_s)

                y1 = function_1(x)
                y2 = function_2(x)


            output_line = "{0: 7.2f}    {1:7.2f}    {2:9.4f}".format (x, y1, y2)

            print (output_line)
            output_file.write(output_line + "\n")