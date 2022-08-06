class CssSelector:
    def __init__(self, html_tag, property_name, property_value, additional_property_name=None,
                 additional_property_value=None):
        if additional_property_name:
            if property_name != 'class' and property_name != 'id':
                raise AttributeError('First property name should be "class" or "id" to add additional selector')
            if not additional_property_value:
                raise AttributeError('you need to add additional property value')
        self.html_tag = html_tag
        self.property_name = property_name
        self.property_value = property_value
        self.additional_property_name = additional_property_name
        self.additional_property_value = additional_property_value

    def _create_first_level(self):
        if self.property_name == 'class':
            return f'{self.html_tag}.{self.property_value}'
        elif self.property_name == 'id':
            return f'{self.html_tag}#{self.property_value}'
        else:
            return f'{self.html_tag}[{self.property_name}={self.property_value}]'

    def __repr__(self):
        if self.additional_property_name:
            return f'{self._create_first_level()}[{self.additional_property_name}={self.additional_property_value}]'
        else:
            return self._create_first_level()
