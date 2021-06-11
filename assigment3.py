Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def list_benefits():
	return benefit_list

>>> benefit_list = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code togather"]
>>> def build_sentence(benefit):
	return benefit + " is a benefit of functions!"

>>> list_of_benefits = list_benefits()
>>> print(build_sentence(list_of_benefits[0]))
More organized code is a benefit of functions!
>>> print(build_sentence(list_of_benefits[1]))
More readable code is a benefit of functions!
>>> print(build_sentence(list_of_benefits[2]))
Easier code reuse is a benefit of functions!
>>> print(build_sentence(list_of_benefits[3]))
Allowing programmers to share and connect code togather is a benefit of functions!
>>> 