

class PC:
    def __init__(self, cpu_cores, memory, storage, price, gpu_serires=None):
        self.cpu = cpu_cores
        self.memory = memory  # in GB
        self.storage = storage  # in GB
        self.gpu = gpu_serires
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"

    def get_specs(self):
        return f"""
        Brand: {self.brand}
        Model: {self.model}
        CPU: {self.cpu}
        Memory: {self.memory} GB
        Storage: {self.storage} GB
        GPU: {self.gpu}
        Price: ${self.price}
        """

    def upgrade_memory(self, additional_memory):
        self.memory += additional_memory
        self.price += additional_memory * 10  # Assuming $10 per GB

    def upgrade_storage(self, additional_storage):
        self.storage += additional_storage
        self.price += additional_storage * 0.2  # Assuming $0.20 per GB

    def is_within_budget(self, budget):
        return self.price <= budget

    def calculate_value_score(self):
        # A simple value score calculation (higher is better)
        return (self.memory + self.storage) / self.price * 1000