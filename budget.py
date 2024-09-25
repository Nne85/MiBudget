class Budget:
    def __init__(self):
        self.overall_budget = 0
        self.category_budgets = {}

    def set_overall_budget(self, amount):
        self.overall_budget = amount

    def set_category_budget(self, category, amount):
        self.category_budgets[category] = amount

    def get_overall_budget(self):
        return self.overall_budget

    def get_category_budget(self, category):
        return self.category_budgets.get(category, 0)

    def get_all_category_budgets(self):
        return self.category_budgets