class Planet:
    def count_age(self, earth_years, planet):
        stala = earth_years / 31557600
        if planet == 'Ziemia':
            return round(stala, 2)
        elif planet == 'Merkury':
            return round(stala / 0.2408467, 2)
        elif planet == 'Wenus':
            return round(stala / 0.61519726, 2)
        elif planet == 'Mars':
            return round(stala / 1.8808158, 2)
        elif planet == 'Jowisz':
            return round(stala / 11.862615, 2)
        elif planet == 'Saturn':
            return round(stala / 29.447498, 2)
        elif planet == 'Uran':
            return round(stala / 84.016846, 2)
        elif planet == 'Neptun':
            return round(stala / 164.79132, 2)
        return ''
