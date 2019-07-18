simple = 100000
compound = 100000
m_year = 1
while simple >= compound:
    simple = simple * (1 + 0.1 ** m_year)
    compound = compound * ((1 + 0.05) ** m_year)
    m_year += 1

print(m_year)
print(simple)
print(compound)
