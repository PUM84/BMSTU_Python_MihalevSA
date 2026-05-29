import re

class LogParser:
    def __init__(self, filename):
        self.filename = filename
        self.ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        self.error_pattern = r'\s(200|401|403|404|500)\s'
        self.method_url_pattern = r'"(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH)\s([^"]+)\sHTTP/\d\.\d"'

    def read_lines(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return f.readlines()

    def extract_ips(self, lines):
        ips = []
        for line in lines:
            match = re.search(self.ip_pattern, line)
            if match:
                ips.append(match.group())
        return ips

    def extract_error_codes(self, lines):
        errors = []
        for line in lines:
            match = re.search(self.error_pattern, line)
            if match:
                errors.append(match.group(1))
        return errors

    def extract_method_url(self, lines):
        requests = []
        for line in lines:
            match = re.search(self.method_url_pattern, line)
            if match:
                requests.append((match.group(1), match.group(2)))
        return requests

    def run(self):
        lines = self.read_lines()
        ips = self.extract_ips(lines)
        errors = self.extract_error_codes(lines)
        requests = self.extract_method_url(lines)

        print("=" * 60)
        print("IP-адреса:")
        for ip in ips:
            print(ip)
        print("\nКоды ошибок:")
        for code in errors:
            print(code)
        print("\nМетод и URL:")
        for method, url in requests:
            print(f"{method} {url}")
        print("=" * 60)


if __name__ == "__main__":
    parser = LogParser("input.txt")
    parser.run()