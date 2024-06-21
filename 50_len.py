# Валідуваті опис (не більше 120 символів)
MAX_DESCRIPSTION_VALUE = 10

response_body = {
    "corse_name" : "Math",
    "descpription": (
        "Lorem issum dolor sit amet, consectetur adipiscint elit"
    ),
}

print((response_body["descpription"]))
print(len(response_body["descpription"]))


if len(response_body["descpription"]) >= MAX_DESCRIPSTION_VALUE:
    print("The description is too long")