class Instrument:

    def __init__(self, name, inst_type, display_name, pip_location, display_precision, trade_units_precision, margin_rate):
        self.name = name
        self.inst_type = inst_type
        self.display_name = display_name
        self.pip_location = pow(10, pip_location)
        self.display_precision = display_precision
        self.trade_units_precision = trade_units_precision
        self.margin_rate = float(margin_rate)

    def __repr__(self):
        return str(vars(self))

    @classmethod
    def FromApiObject(cls, obj):
        return Instrument(
            obj['name'],
            obj['type'],
            obj['displayName'],
            obj['pipLocation'],
            obj['displayPrecision'],
            obj['tradeUnitsPrecision'],
            obj['marginRate']
        )
