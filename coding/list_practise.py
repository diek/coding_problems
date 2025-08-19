sample_list = ["Jon", "Kelly", "Jessa"]
sample_list.append([2, "Scott"])
print(sample_list)
sample_list.extend(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
print(sample_list)
sample_list.extend("A")
print(sample_list)
sample_list.extend(
    (
        "E",
        "F",
    )
)
print(sample_list)
sample_list.append("Z")
print(sample_list)
sample_list.pop("Z")
print(sample_list)
