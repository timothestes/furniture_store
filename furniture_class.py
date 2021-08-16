class FancyFurnitureStore:
    def __init__(
        self,
        storeManager: str,
        allStoreManagers: dict = {},
        version: int = 1,
        **kwargs,
    ):
        self.version = version
        self.storeManager = storeManager

        # allStoreManagers should initialize to {} right??
        self.allStoreManagers = allStoreManagers

        if str(self.version) not in self.allStoreManagers.keys():
            self.allStoreManagers[str(self.version)] = self.storeManager

    def to_dict(self):
        return self.__dict__