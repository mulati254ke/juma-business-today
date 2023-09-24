class BusinessUnit:
  def __init__(self, name, description, advantages, disadvantages):
    self.name = name
    self.description = description
    self.advantages = advantages
    self.disadvantages = disadvantages

  def __str__(self):
    return self.name

# Create a list of business units
business_units = [
  BusinessUnit("Sole proprietorship", "A business owned and operated by one person.", ["Easy to start and manage", "Complete control over the business", "All profits go to the owner"], ["Unlimited liability", "No access to capital", "Limited resources and expertise"]),
  BusinessUnit("Partnership", "A business owned and operated by two or more people.", ["Easy to start and manage", "Shared resources and expertise", "Quick decision-making"], ["Unlimited liability", "Disagreements and disputes", "Different levels of commitment and involvement"]),
  BusinessUnit("Limited liability company (LLC)", "A business entity that has a separate legal entity from its owners.", ["Limited liability", "Access to capital", "Separate legal entity"], ["More difficult and expensive to form and maintain", "Subject to government regulation"]),
  BusinessUnit("Cooperative", "A business owned and controlled by its members.", ["Member ownership and control", "Shared profits and losses", "Democratic decision-making"], ["May be difficult to manage", "Less efficient than other types of business units"]),
  BusinessUnit("Public corporation", "A business that is owned by shareholders and is traded on a public stock exchange.", ["Access to capital", "Limited liability", "Perpetual existence"], ["Subject to public scrutiny", "More complex and expensive to manage", "Double taxation"]),
]

# Print the list of business units
for business_unit in business_units:
  print(business_unit)
