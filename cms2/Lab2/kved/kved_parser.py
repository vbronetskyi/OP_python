"""Lab_2.Ex_1: kved.json"""
import json

def write_in_file(data: str)->None:
    """
    Writes the result to a "kved_results.json" file
    >>> write_in_file({'name': "Комп'ютерне програмування", 'type': 'class', 'parent': {'name': \
    "Комп'ютерне програмування, консультування та пов'язана з ними діяльність", 'type'\
    : 'group', 'num_children': 4, 'parent': {'name': "Комп'ютерне програмування, \
    консультування та пов'язана з ними діяльність", 'type': 'division', 'num_children': \
    1, 'parent': {'name': 'Інформація та телекомунікації', 'type': 'section', 'num_children': \
    6}}}})
    """
    with open("kved_results.json", 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii = False)
    return None

def parse_kved(class_code: str)->None:
    """
    Searches for a class of code, then creates a path to it,
    and writes it to a file using an additional function
    >>> parse_kved(62.01)
    """
    file = open('kved.json', encoding = 'utf-8')
    kveds = json.load(file)
    for kved in kveds["sections"][0]:
        for division in kved["divisions"]:
            for group in division["groups"]:
                for group_class in group['classes']:
                    if group_class['classCode'] == str(class_code):
                        name1 = group_class['className']
                        data = {
                            "name": name1,
                            "type": 'class',
                            "parent": {
                                "name": group['groupName'],
                                "type": 'group',
                                "num_children": len(group['classes']),
                                "parent": {
                                    "name": division["divisionName"],
                                    "type": "division",
                                    "num_children": len(division["groups"]),
                                    "parent": {
                                        "name": kved["sectionName"],
                                        "type": "section",
                                        "num_children": len(kved["divisions"]),
                                    }
                                }
                            }
                        }
                        write_in_file(data)
                        return None

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
