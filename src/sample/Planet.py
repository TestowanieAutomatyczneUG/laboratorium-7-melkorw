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
        return ''
