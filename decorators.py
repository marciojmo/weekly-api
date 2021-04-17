def singleton(cls):
    cls.__instance__ = None
    
    def get_instance():
        """
        Returns a singleton instance of the TaskService.
        
        Returns:
            A singleton instance of the TaskService.
        """
        if not cls.__instance__:
            cls.__instance__ = cls()
        return cls.__instance__
    
    cls.get_instance = get_instance
    return cls