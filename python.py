import xml.etree.ElementTree as ET


def przetworz_xml(sciezka_do_pliku):
    try:
        tree = ET.parse(sciezka_do_pliku)
        root = tree.getroot()

        # Przeglądamy bezpośrednich rodziców (np. KeyBindingCategoryDef, KeyBindingDef)
        for obj in root:
            def_name_elem = obj.find("defName")

            # Warunek: obiekt musi posiadać znacznik <defName>
            if def_name_elem is not None and def_name_elem.text:
                def_name = def_name_elem.text.strip()

                label_elem = obj.find("label")
                desc_elem = obj.find("description")

                if label_elem is not None and label_elem.text:
                    print(
                        f"<{def_name}.label>{label_elem.text.strip()}</{def_name}.label>"
                    )

                if desc_elem is not None and desc_elem.text:
                    print(
                        f"<{def_name}.description>{desc_elem.text.strip()}</{def_name}.description>"
                    )

    except FileNotFoundError:
        print(f"Błąd: Plik '{sciezka_do_pliku}' nie został odnaleziony.")
    except ET.ParseError:
        print(f"Błąd: Plik '{sciezka_do_pliku}' nie jest poprawnym plikiem XML.")


if __name__ == "__main__":
    przetworz_xml("./moj_plik.xml")  # Zmień nazwę pliku na swoją
