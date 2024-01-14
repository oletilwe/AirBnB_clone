import unittest
from unittest.mock import patch
from your mode import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def test_do_create(self, mock_input:
        hbnb_command = HBNBCommand()
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                hbnb_command.onecmd("create BaseModel")
                output = mock_stdout.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

class TestDoShow(unittest.TestCase):
    """TestCase for the do show method"""

    def setUp(self):
        self.your_instance = do_show()

    def Test_show_invalid_class_name(self, mock_print):
        self.your_instance.do_show("")
        mock_print.assert_called_with("** class name missing **")

    def test_show_invalid_class_name(self, mock_print):
        self.your_instance.do_show("InvalidClassName")
        mock_print.assert_called_with("** class doesn't exist **")

     def test_show_missing_instance_id(self, mock_print):
        self.your_instance.do_show("BaseModel")
        mock_print.assert_called_with("** instance id missing **")

    def test_show_no_instance_found(self, mock_print):
        with patch('your_module.storage.all', return_value={}):  // replace with actual module and function
            self.your_instance.do_show("BaseModel 123")
        mock_print.assert_called_with("** no instance found **")

    def test_show_instance_found(self, mock_print):
        with patch('your_module.storage.all', return_value={"BaseModel.123": "Instance"}):  // replace with actual values
            self.your_instance.do_show("BaseModel 123")
        mock_print.assert_called_with("Instance")


class TestDoDestroyMethod(unittest.TestCase):
    """TestCase for the do destroy method"""

    def setUp(self):
        self.your_instance = do_destroy()

   def test_destroy_missing_class_name(self, mock_print):
        self.your_instance.do_destroy("")
        mock_print.assert_called_with("** class name missing **")

    def test_destroy_invalid_class_name(self, mock_print):
        self.your_instance.do_destroy("InvalidClassName")
        mock_print.assert_called_with("** class doesn't exist **")

    def test_destroy_missing_instance_id(self, mock_print):
        self.your_instance.do_destroy("BaseModel")
        mock_print.assert_called_with("** instance id missing **")

    def test_destroy_no_instance_found(self, mock_print):
        with patch('your_module.storage.all', return_value={}):  # replace with actual module and function
            self.your_instance.do_destroy("BaseModel 123")
        mock_print.assert_called_with("** no instance found **")

    def test_destroy_instance_found(self, mock_save, mock_all):
        self.your_instance.do_destroy("BaseModel 123")
        mock_save.assert_called_once()
        mock_all.assert_called_once()

class TestDoAll(unittest.TestCase):
    """TestCase for the do all method"""

    def setUp(self):
        self.your_instance = do_all()

    def test_all_no_class_specified(self, mock_all, mock_print):
        self.your_instance.do_all("")
        mock_all.assert_called_once()
        mock_print.assert_called_with(["Instance1", "Instance2"])

    def test_all_invalid_class_name(self, mock_print):
        self.your_instance.do_all("InvalidClassName")
        mock_print.assert_called_with("** class doesnt exist **")

    def test_all_valid_class_name(self, mock_all, mock_print):
        self.your_instance.do_all("BaseModel")
        mock_all.assert_called_once()
        mock_print.assert_called_with(["Instance1"])

    def test_all_valid_class_name_with_instance(self, mock_all, mock_print):
        self.your_instance.do_all("User")
        mock_all.assert_called_once()
        mock_print.assert_called_with(["Instance2"])

class TestDoUpdateMethod(unittest.TestCase):
    """testCase for the do update method"""

    def setUp(self):
        self.your_instance = do_update()

    def test_update_missing_class_name(self, mock_print):
        self.your_instance.do_update("")
        mock_print.assert_called_with("** class name missing **")

    def test_update_invalid_class_name(self, mock_print):
        self.your_instance.do_update("InvalidClassName")
        mock_print.assert_called_with("** class doesn't exist **")

    def test_update_missing_instance_id(self, mock_print):
        self.your_instance.do_update("BaseModel")
        mock_print.assert_called_with("** instance id missing **")

    def test_update_no_instance_found(self, mock_all, mock_print):
        self.your_instance.do_update("BaseModel 123")
        mock_all.assert_called_once()
        mock_print.assert_called_with("** no instance found **")

    def test_update_missing_attribute_name(self, mock_all, mock_print):
        self.your_instance.do_update("BaseModel 123")
        mock_all.assert_called_once()
        mock_print.assert_called_with("** attribute name missing **")

    def test_update_missing_value(self, mock_all, mock_print):
        self.your_instance.do_update("BaseModel 123 attribute_name")
        mock_all.assert_called_once()
        mock_print.assert_called_with("** value missing **")

    def test_update_successful(self, mock_save, mock_all):
        self.your_instance.do_update("BaseModel 123 attribute_name 'new_value'")
        mock_all.assert_called_once()
        mock_save.assert_called_once()

class TestDoQuit(unittest.TestCase):
    """testCase for the do quit method"""

    def setUp(self):
        self.your_instance = do_quit()

     def test_quit(self):
        result = self.your_instance.do_quit("")
        self.assertTrue(result)

class testDoEOF(unittest.TestCase):
    """testCase for the do EOF method"""

    def setUp(self):
        self.your_instance = do_EOF()

    def test_do_EOF(self, mock_print):
        with patch('builtins.print') as mock_print:
            result = self.your_instance.do_EOF("")
            self.assertTrue(result)
            mock_print.assert_called_once_with()

class TestEmptyLine(unnittest.TestCase):
    """testcase for the empty method"""

    def setUp(self):
        self.your_instance = emptyLine()

    def test_emptyline(self):
        with self.assertDoesNotRaise(Exception):
            self.your_instance.emptyline("")

if __name__ == '__main__':
    unittest.main()
