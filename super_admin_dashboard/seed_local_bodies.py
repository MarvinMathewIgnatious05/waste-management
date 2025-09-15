
from super_admin_dashboard.models import State, District, LocalBody

def run():
    # State
    kerala, _ = State.objects.get_or_create(name="Kerala")

    # --- Kottayam ---
    kottayam, _ = District.objects.get_or_create(state=kerala, name="Kottayam")
    kottayam_municipalities = [
        "Changanassery",
        "Erattupetta",
        "Ettumanoor",
        "Kottayam",
        "Palai (Pala)",
        "Vaikom",
    ]
    for name in kottayam_municipalities:
        LocalBody.objects.get_or_create(
            district=kottayam, name=name, body_type="municipality"
        )

    # --- Ernakulam ---
    ernakulam, _ = District.objects.get_or_create(state=kerala, name="Ernakulam")
    LocalBody.objects.get_or_create(
        district=ernakulam, name="Kochi", body_type="corporation"
    )
    for name in ["Aluva", "Kalamassery"]:
        LocalBody.objects.get_or_create(
            district=ernakulam, name=name, body_type="municipality"
        )

    # --- Thrissur ---
    thrissur, _ = District.objects.get_or_create(state=kerala, name="Thrissur")

    thrissur_municipalities = ["Chalakudy", "Chavakkad", "Guruvayur", "Irinjalakkuda"]
    for name in thrissur_municipalities:
        LocalBody.objects.get_or_create(
            district=thrissur, name=name, body_type="municipality"
        )

    thrissur_panchayats = ["Anthikkad", "Chalakudy", "Chavakkad"]
    for name in thrissur_panchayats:
        LocalBody.objects.get_or_create(
            district=thrissur, name=name, body_type="panchayat"
        )

    print("✅ Kerala, districts, and local bodies seeded successfully!")
