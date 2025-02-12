import pytest
import source.to_do as todo

class TestComplete:
    # Runs in the beginning of every test
    def setup_method(self,method):
        print(f"Setting up {method}")
        self.value = False
    # Runs after the end of every test
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.value

    def test_get_value(self):
        assert todo.Complete.get_value(self) == False

    @pytest.mark.parametrize("set_val", (True, False))
    def test_set_value(self, set_val):
        todo.Complete.set_value(self, set_val)
        assert todo.Complete.get_value(self) == set_val

    def test_toggle_value(self):
        todo.Complete.toggle_value(self)
        assert todo.Complete.get_value(self) is self.value