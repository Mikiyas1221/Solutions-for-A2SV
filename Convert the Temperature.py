class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + float(273.15)
        fahrenheit = celsius * float(1.80) + float(32.00)
        return [float(kelvin), float(fahrenheit)]
        
