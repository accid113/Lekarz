class Diagnosis:
    def __init__(self):
        self.symptoms = {
            'niedoczynnosc_tarczycy': {
                'tsh': (0.5, 5.0),
                'ft4': (0.8, 2.0)
            },
            'nadczynnosc_tarczycy': {
                'tsh': (0.1, 0.5),
                'ft4': (2.0, 4.0)
            },
            'cukrzyca_typu_1': {
                'glukoza': (200, None),
                'insulina': (15, None),
                'obecnosc_przeciwcial': True
            },
            'cukrzyca_typu_2': {
                'glukoza': (140, 200),
                'insulina': (15, None),
                'obecnosc_przeciwcial': False
            }
        }

    def suggest_diseases(self, test_results):
        suggested_diseases = []
        for disease, criteria in self.symptoms.items():
            is_possible_disease = True
            for parameter, value in criteria.items():
                if parameter == 'obecnosc_przeciwcial':
                    expected_value = value
                    actual_value = test_results.get(parameter, False)
                    if actual_value != expected_value:
                        is_possible_disease = False
                        break
                elif parameter in test_results:
                    min_value, max_value = value
                    actual_value = test_results[parameter]
                    if max_value is None:
                        if actual_value < min_value:
                            is_possible_disease = False
                            break
                    else:
                        if not (min_value <= actual_value < max_value):
                            is_possible_disease = False
                            break
                else:
                    is_possible_disease = False
                    break
            if is_possible_disease:
                suggested_diseases.append(disease)
        return suggested_diseases


def main():
    diagnosis = Diagnosis()

    test_results = {
        'tsh': 4,
        'ft4': 1,
        'glukoza': 180,
        'insulina': 25,
        'obecnosc_przeciwcial': False
    }

    suggested_diseases = diagnosis.suggest_diseases(test_results)
    if suggested_diseases:
        print("Możliwe choroby na podstawie wyników badań medycznych:")
        for disease in suggested_diseases:
            print("-", disease)
    else:
        print("Nie wykryto żadnych zaburzeń podstawie wyników badań medycznych.")


if __name__ == "__main__":
    main()
