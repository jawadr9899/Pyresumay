from lxml import etree, html
from typing import TypedDict


class BuildCV:
    class CVDat(TypedDict):
        _name: None | str | etree._Element
        _occupation: None | str | etree._Element
        _email: None | str | etree._Element
        _phone: None | str | etree._Element
        _place: None | str | etree._Element
        _about: None | str | etree._Element
        _wrk_expr: None | str | etree._Element
        _education: None | str | etree._Element
        _skills: None | str | etree._Element

    def __init__(self, path: str):
        self.tree: etree._ElementTree = etree.parse(path)
        self.attrs: self.CVDat = {
            "_name": None,
            "_occupation": None,
            "_email": None,
            "_phone": None,
            "_place": None,
            "_about": None,
            "_wrk_expr": None,
            "_education": None,
            "_skills": None,
        }
        self._assign()

    def _assign(self):
        for k, _ in self.attrs.items():
            elm = self.tree.find(f""".//*[@id="{k}"]""")
            self.attrs[k] = elm if elm is not None else None

    def populate(self, data: CVDat):
        for k, _ in self.attrs.items():
            if k == "_skills":
                continue
            self.attrs[k].text = data[k]

        skills = data["_skills"].split(",")
        for i, k in enumerate(skills):
            elem = html.Element("li")
            elem.text = k
            skills[i] = elem
            self.attrs["_skills"].append(elem)
    
        # build
        self.tree.write("templates/website/build.html")
