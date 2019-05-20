from unittest.mock import Mock, DEFAULT

mock_ins = Mock(return_value='return_value', side_effect=None)
print(mock_ins())