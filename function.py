from abc import ABC, abstractmethod


class call(ABC):
    @abstractmethod
    def greeting(self, name):
        """Return a personalized greeting for the provided name."""
        raise NotImplementedError

    @abstractmethod
    def welcome(self):
        """Return the app's welcome message."""
        raise NotImplementedError

    def __call__(self, name):
        print(self.greeting(name))
        print(self.welcome())


class SimpleCall(call):
    def greeting(self, name):
        return f"Hello {name}!"

    def welcome(self):
        return "Welcome to programming!"


def great(name):
    runner = SimpleCall()
    runner(name)


great("saidi")
great("mohammed")

def make_full_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name
name = make_full_name("saidi", "tsuma")
print(name)
