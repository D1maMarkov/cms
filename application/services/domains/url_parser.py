import re

from application.common.url_parser import UrlParserInterface


class UrlParser(UrlParserInterface):
    def get_subdomain_from_host(self, host: str) -> str:
        host = self.remove_protocol(host)
        host = host.replace("127.0.0.1", "localhost")

        if "localhost" in host:
            if "." not in host:
                return ""

            return host.split(".")[0]

        if host.count(".") < 2:
            return ""

        return host.split(".")[0]

    def get_domain_from_host(self, host: str) -> str:
        host = self.remove_protocol(host)
        host = host.replace("127.0.0.1", "localhost")

        if ":" in host:
            host = host.split(":")[0]

        subdomain = self.get_subdomain_from_host(host)
        first_domain = host.split(".")[-1]

        domain = re.findall(f"{subdomain}.*?{first_domain}", host)[0]
        domain = re.sub(subdomain, "", domain)
        if domain[0] == ".":
            domain = domain[1::]

        return domain

    @staticmethod
    def remove_protocol(path: str) -> str:
        path = path.replace("https://", "")
        path = path.replace("http://", "")

        return path


def get_url_parser() -> UrlParserInterface:
    return UrlParser()
