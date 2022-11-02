class DataValidation:
    @staticmethod
    def field_not_empty(value):
        if not value.strip():
            raise ValueError('Field cannot be empty or whitespace.')

        return value

    @staticmethod
    def field_not_numeric(value):
        if value and not value.isalpha():
            raise ValueError('Field cannot contain numbers.')

        return value

    @classmethod
    def field_positive_number(cls, value):
        if value < 0:
            raise ValueError('Field must be a positive number.')

        return value
