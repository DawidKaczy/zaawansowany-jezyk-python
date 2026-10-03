class ServerConfig:
    def __init__(self, host, /, port, *, timeout, max_retries):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.max_retries = max_retries

    def __repr__(self):
        return (f"ServerConfig(host='{self.host}', port={self.port}, "
                f"timeout={self.timeout}, max_retries={self.max_retries})")


