import streamlit as st
import json
from datetime import datetime

st.set_page_config(
    page_title="AI-Driven Travel Agency Booking Demo",
    layout="wide",  # This makes the layout wide (100% width)
    initial_sidebar_state="expanded"
)

# -----------------------
# 1. DATA AND LOOKUPS
# -----------------------
users_data = [
    {
        "user_id": "u1",
        "name": "Ahmed Al Reesi",
        "email": "alice.johnson@example.com",
        "persona": "Tech Enthusiast",
        "preferences": {
            "interests": ["AI", "Tech"],
            "preferred_price_range": {"min": 100, "max": 250}
        },
        "interested_event_types": ["Technology", "Business"],
        "bookings": [
            {
                "booking_id": "b1001",
                "hotel_id": "h103",  # Singapore City Inn
                "location_id": "ci4",  # Singapore
                "booking_date": "2023-05-20",
                "event_id": "e101"     # Singapore Tech Week 2024
            },
            {
                "booking_id": "b1002",
                "hotel_id": "h104",  # Dubai Downtown Hotel
                "location_id": "ci5",  # Dubai
                "booking_date": "2023-06-10",
                "event_id": "e102"    # Dubai Tech Expo 2024
            }
        ]
    },
    {
        "user_id": "u2",
        "name": "Maryam Al Rasbi",
        "email": "bob.smith@example.com",
        "persona": "Luxury Seeker",
        "preferences": {
            "interests": ["Culture", "Spa", "Beach", "Luxury"],
            "preferred_price_range": {"min": 200, "max": 500}
        },
        "interested_event_types": ["Culture & Spa"],
        "bookings": [
            {
                "booking_id": "b2001",
                "hotel_id": "h100",   # Bali Paradise Resort
                "location_id": "ci1", # Bali
                "booking_date": "2024-02-15",
                "event_id": "e100"    # Bali Culture & Wellness Fest 2024
            },
            {
                "booking_id": "b2002",
                "hotel_id": "h109",   # Phuket Beach Resort
                "location_id": "ci6", # Phuket
                "booking_date": "2024-12-20",
                "event_id": "e999"    # Phuket Spa & Culture Expo 2025
            }
        ]
    },
    {
        "user_id": "u3",
        "name": "Mohammad Raza",
        "email": "charlene.wang@example.com",
        "persona": "Business Professional",
        "preferences": {
            "interests": ["Tech", "Business", "City Tours"],
            "preferred_price_range": {"min": 200, "max": 400}
        },
        "interested_event_types": ["Business", "Technology"],
        "bookings": [
            {
                "booking_id": "b3001",
                "hotel_id": "h103",   # Singapore City Inn
                "location_id": "ci4", # Singapore
                "booking_date": "2024-03-20",
                "event_id": "e202"    # Singapore Business Summit 2024
            },
            {
                "booking_id": "b3002",
                "hotel_id": "h110",   # Paris Boutique Inn
                "location_id": "ci7", # Paris
                "booking_date": "2024-09-01",
                "event_id": "e110"    # Paris Tech Summit 2024
            }
        ]
    }
]

hotels_data = [
    {
        "hotel_id": "h100",
        "name": "Bali Paradise Resort",
        "location_id": "ci1",
        "amenities": ["Pool", "WiFi", "Spa", "Gym", "Beach Access"],
        "price_per_night": 150,
        "rating": 4.5,
        "available_dates": ["2024-06-14", "2024-06-16"],
        "themes": ["Beach", "Leisure", "Wellness", "Resort"],
        "associated_event_ids": ["e100"]  # Tied to Bali Culture & Wellness Fest
    },
    {
        "hotel_id": "h101",
        "name": "Mauritius Beach Hotel",
        "location_id": "ci2",
        "amenities": ["Pool", "WiFi", "Beach Access", "Gym", "Restaurant"],
        "price_per_night": 200,
        "rating": 4.7,
        "available_dates": ["2024-07-01", "2024-07-15"],
        "themes": ["Beach", "Leisure", "Resort"],
        "associated_event_ids": []  # No direct event association for demo
    },
    {
        "hotel_id": "h102",
        "name": "Maldives Luxury Stay",
        "location_id": "ci3",
        "amenities": ["Pool", "WiFi", "Private Beach", "Spa", "Water Sports"],
        "price_per_night": 300,
        "rating": 4.8,
        "available_dates": ["2024-12-01", "2024-12-15"],
        "themes": ["Beach", "Luxury", "Spa", "Resort"],
        "associated_event_ids": []
    },
    {
        "hotel_id": "h103",
        "name": "Singapore City Inn",
        "location_id": "ci4",
        "amenities": ["WiFi", "Gym", "Conference Rooms", "Restaurant", "Bar"],
        "price_per_night": 180,
        "rating": 4.3,
        "available_dates": ["2024-08-14", "2024-08-16", "2024-04-14", "2024-04-16"],
        "themes": ["City", "Business", "Tech-Friendly"],
        "associated_event_ids": ["e101", "e202"]  # Tied to Singapore Tech Week & Business Summit
    },
    {
        "hotel_id": "h104",
        "name": "Dubai Downtown Hotel",
        "location_id": "ci5",
        "amenities": ["Pool", "WiFi", "Spa", "Gym", "Conference Rooms", "Rooftop Lounge"],
        "price_per_night": 250,
        "rating": 4.6,
        "available_dates": ["2024-03-09", "2024-03-11"],
        "themes": ["Business", "Tech-Friendly", "Luxury"],
        "associated_event_ids": ["e102"]  # Dubai Tech Expo
    },
    {
        "hotel_id": "h105",
        "name": "Mauritius Luxury Villas",
        "location_id": "ci2",
        "amenities": ["Private Pool", "WiFi", "Spa", "Beach Access", "Butler Service"],
        "price_per_night": 350,
        "rating": 4.9,
        "available_dates": ["2024-07-10", "2024-07-20"],
        "themes": ["Beach", "Luxury", "Spa", "Resort"],
        "associated_event_ids": []
    },
    {
        "hotel_id": "h106",
        "name": "Maldives Coral Retreat",
        "location_id": "ci3",
        "amenities": ["Overwater Bungalows", "WiFi", "Spa", "Diving Center", "Infinity Pool"],
        "price_per_night": 320,
        "rating": 4.7,
        "available_dates": ["2024-12-10", "2024-12-20"],
        "themes": ["Beach", "Luxury", "Spa", "Resort"],
        "associated_event_ids": []
    },
    {
        "hotel_id": "h107",
        "name": "Singapore Riverside Suites",
        "location_id": "ci4",
        "amenities": ["WiFi", "Gym", "Breakfast Included", "Pool", "City View"],
        "price_per_night": 220,
        "rating": 4.4,
        "available_dates": ["2024-08-14", "2024-08-16"],
        "themes": ["City", "Business"],
        "associated_event_ids": []
    },
    {
        "hotel_id": "h108",
        "name": "Bali Zen Retreat",
        "location_id": "ci1",
        "amenities": ["WiFi", "Spa", "Yoga Classes", "Beach Access", "Meditation Garden"],
        "price_per_night": 170,
        "rating": 4.5,
        "available_dates": ["2024-06-14", "2024-06-16"],
        "themes": ["Beach", "Wellness", "Resort"],
        "associated_event_ids": ["e100"]
    },
    {
        "hotel_id": "h109",
        "name": "Phuket Beach Resort",
        "location_id": "ci6",
        "amenities": ["Pool", "WiFi", "Beach Access", "Spa", "Water Sports"],
        "price_per_night": 200,
        "rating": 4.6,
        "available_dates": ["2025-02-01", "2025-02-10"],
        "themes": ["Beach", "Wellness", "Leisure", "Resort"],
        "associated_event_ids": ["e999"]  # Phuket Spa & Culture Expo
    },
    {
        "hotel_id": "h110",
        "name": "Paris Boutique Inn",
        "location_id": "ci7",
        "amenities": ["WiFi", "City View", "Breakfast Included", "Gym", "Concierge"],
        "price_per_night": 250,
        "rating": 4.5,
        "available_dates": ["2024-10-14", "2024-10-16"],
        "themes": ["City", "Business", "Culture"],
        "associated_event_ids": ["e110"]  # Paris Tech Summit
    },
    {
        "hotel_id": "h999",
        "name": "Phuket Spa Resort",
        "location_id": "ci6",
        "amenities": ["Pool", "WiFi", "Spa", "Beach Access"],
        "price_per_night": 400,
        "rating": 4.8,
        "available_dates": ["2025-02-05", "2025-02-15"],
        "themes": ["Beach", "Luxury", "Spa", "Resort"],
        "associated_event_ids": ["e999"]
    }
]

countries_data = [
    {"country_id": "c1", "name": "Indonesia"},
    {"country_id": "c2", "name": "Mauritius"},
    {"country_id": "c3", "name": "Maldives"},
    {"country_id": "c4", "name": "Singapore"},
    {"country_id": "c5", "name": "United Arab Emirates"},
    {"country_id": "c6", "name": "Thailand"},
    {"country_id": "c7", "name": "France"}
]

cities_data = [
    {"city_id": "ci1", "name": "Bali", "country_id": "c1"},
    {"city_id": "ci2", "name": "Port Louis", "country_id": "c2"},
    {"city_id": "ci3", "name": "Malé", "country_id": "c3"},
    {"city_id": "ci4", "name": "Singapore", "country_id": "c4"},
    {"city_id": "ci5", "name": "Dubai", "country_id": "c5"},
    {"city_id": "ci6", "name": "Phuket", "country_id": "c6"},
    {"city_id": "ci7", "name": "Paris", "country_id": "c7"}
]

events_data = [
    {
        "event_id": "e100",
        "name": "Bali Culture & Wellness Fest 2024",
        "location_id": "ci1",
        "date": "2024-06-15",
        "type": "Culture & Wellness"
    },
    {
        "event_id": "e101",
        "name": "Singapore Tech Week 2024",
        "location_id": "ci4",
        "date": "2024-08-15",
        "type": "Technology"
    },
    {
        "event_id": "e102",
        "name": "Dubai Tech Expo 2024",
        "location_id": "ci5",
        "date": "2024-03-10",
        "type": "Technology"
    },
    {
        "event_id": "e104",
        "name": "Malé Surfing Festival 2024",
        "location_id": "ci3",
        "date": "2024-12-01",
        "type": "Sports"
    },
    {
        "event_id": "e110",
        "name": "Paris Tech Summit 2024",
        "location_id": "ci7",
        "date": "2024-10-15",
        "type": "Technology"
    },
    {
        "event_id": "e999",
        "name": "Phuket Spa & Culture Expo 2025",
        "location_id": "ci6",
        "date": "2025-02-01",
        "type": "Culture & Spa"
    },
    {
        "event_id": "e202",
        "name": "Singapore Business Summit 2024",
        "location_id": "ci4",
        "date": "2024-04-15",
        "type": "Business"
    }
]

# Dictionaries for quick lookups
hotels_dict = {h["hotel_id"]: h for h in hotels_data}
cities_dict = {c["city_id"]: c for c in cities_data}
countries_dict = {cn["country_id"]: cn for cn in countries_data}
events_dict = {e["event_id"]: e for e in events_data}


def get_user_by_id(user_id):
    for user in users_data:
        if user["user_id"] == user_id:
            return user
    return None


def get_hotel_by_id(hotel_id):
    return hotels_dict.get(hotel_id, None)


def get_event_by_id(event_id):
    return events_dict.get(event_id, None)


def get_city_name(location_id):
    city_info = cities_dict.get(location_id)
    return city_info["name"] if city_info else "Unknown City"


def get_country_name(location_id):
    city_info = cities_dict.get(location_id)
    if city_info:
        country_info = countries_dict.get(city_info["country_id"])
        return country_info["name"] if country_info else "Unknown Country"
    return "Unknown Country"


def book_hotel(user, hotel_id):
    new_booking_id = f"b_new_{int(datetime.now().timestamp())}"
    booking_record = {
        "booking_id": new_booking_id,
        "hotel_id": hotel_id,
        "location_id": hotels_dict[hotel_id]["location_id"],
        "booking_date": str(datetime.now().date()),
        "event_id": None
    }
    user["bookings"].append(booking_record)
    st.success(f"You have booked {hotels_dict[hotel_id]['name']} successfully!")
    st.info(f"Booking ID: {new_booking_id}")


def match_user_preferences(user, hotel):
    """
    Simple boolean check to see if the hotel meets essential user criteria:
    - Price is in the user's preferred range.
    - (Optional) Additional checks on persona-themed alignment.
    """
    prefs = user["preferences"]
    price_min = prefs["preferred_price_range"]["min"]
    price_max = prefs["preferred_price_range"]["max"]
    if not (price_min <= hotel["price_per_night"] <= price_max):
        return False

    # Persona-based or interest-based theme check (optional for stronger filtering)
    # For instance, a Tech Enthusiast might prefer "Tech-Friendly" or "Business" theme
    user_persona = user["persona"]
    persona_theme_map = {
        "Tech Enthusiast": ["Tech-Friendly", "Business"],
        "Luxury Seeker": ["Luxury", "Spa", "Resort"],
        "Business Professional": ["Business", "City", "Tech-Friendly"]
    }
    allowed_themes = persona_theme_map.get(user_persona, [])

    # If the hotel's themes match at least one of the allowed themes for that persona, we consider it relevant.
    # If there's no overlap, we consider it less relevant. This can be as strict or lenient as needed.
    if not any(t in hotel["themes"] for t in allowed_themes):
        return False

    return True


def generate_reasoning(current_user, candidate_hotel):
    """
    Generate a list of reasons why this 'candidate_hotel' is recommended to 'current_user'.
    Factors considered:
    1. User's persona and interests.
    2. Event Type and Date Proximity.
    3. Similarity to Past Bookings.
    4. Price and rating alignment.
    5. Potential event-based synergy (hotel's associated events).
    """
    prefs = current_user["preferences"]
    user_interests = prefs["interests"]
    user_past_bookings = current_user["bookings"]
    user_persona = current_user.get("persona", "Traveler")
    interested_event_types = current_user.get("interested_event_types", [])

    reasons = []

    # ---------------------------
    # (A) User's Persona alignment
    # ---------------------------
    reasons.append(f"Matches your persona as a **{user_persona}**.")

    # ---------------------------
    # (B) Interests to Amenities Mapping
    # ---------------------------
    # Adjust the interest-to-amenity (or theme) mapping to better fit real scenarios
    interest_amenity_map = {
        "Beach": "Beach Access",
        "Spa": "Spa",
        "Luxury": "Butler Service or Private Pool or Overwater Bungalows",
        "Tech": "Conference Rooms",
        "AI": "Conference Rooms",
        "Business": "Conference Rooms",
        "Culture": "Cultural or local experiences",
        "City Tours": "City View"
    }
    # If any interests match the hotel's amenities or themes
    for interest in user_interests:
        target_amenity_or_keyword = interest_amenity_map.get(interest)
        if not target_amenity_or_keyword:
            continue
        # If the amenity is a specific item that can appear in the hotel's amenities list
        # or if we consider "culture" => we do a broader phrase match approach
        # Example: "Butler Service" in the hotel's amenities or "Conference Rooms" in the hotel's amenities
        for a in candidate_hotel["amenities"]:
            if target_amenity_or_keyword in a:
                reasons.append(f"Provides **{a}**, aligning with your interest in '{interest}'.")
        # Themes check if the user interest references certain keywords
        for t in candidate_hotel["themes"]:
            if interest.lower() in t.lower():
                reasons.append(f"Hotel theme '{t}' aligns with your interest in '{interest}'.")

    # ---------------------------
    # (C) Event-based synergy
    # ---------------------------
    # Hotel might have direct associated events or user might be interested in certain event types
    # Also check if there's an upcoming event in the same location or in the 'associated_event_ids'.
    current_date = datetime.now().date()
    # 1) Check direct associated events for the hotel
    if candidate_hotel["associated_event_ids"]:
        for evt_id in candidate_hotel["associated_event_ids"]:
            evt = get_event_by_id(evt_id)
            if evt:
                # If the user is interested in the event type and the event is upcoming
                event_date = datetime.strptime(evt["date"], "%Y-%m-%d").date()
                if (evt["type"] in interested_event_types) and event_date >= current_date:
                    reasons.append(f"Close to your interest: **{evt['name']}** on {evt['date']} ({evt['type']}).")

    # 2) Check other events in the same location matching user interest
    relevant_events = []
    for event in events_data:
        event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()
        if (event["type"] in interested_event_types and
            event["location_id"] == candidate_hotel["location_id"] and
            event_date >= current_date):
            relevant_events.append(event)
    if relevant_events:
        for evt in relevant_events:
            reasons.append(f"Nearby upcoming event: **{evt['name']}** ({evt['type']}) on {evt['date']}.")

    # ---------------------------
    # (D) Similarity to Past Bookings
    # ---------------------------
    for booking in user_past_bookings:
        booked_hotel = get_hotel_by_id(booking["hotel_id"])
        if not booked_hotel:
            continue
        # Similar location check
        if booked_hotel["location_id"] == candidate_hotel["location_id"]:
            city_name = get_city_name(candidate_hotel["location_id"])
            reasons.append(f"You previously stayed in **{city_name}**, and this hotel is also in {city_name}.")
        # Overlapping amenities
        common_amenities = set(booked_hotel["amenities"]).intersection(set(candidate_hotel["amenities"]))
        if common_amenities:
            amenities_str = ", ".join(common_amenities)
            reasons.append(
                f"Shares amenities like **{amenities_str}** with your past stay at {booked_hotel['name']}."
            )

    # ---------------------------
    # (E) Price and Rating
    # ---------------------------
    price_min = prefs["preferred_price_range"]["min"]
    price_max = prefs["preferred_price_range"]["max"]
    reasons.append(f"Within your preferred price range of **{price_min}USD – {price_max}USD**.")
    reasons.append(f"Rated **{candidate_hotel['rating']}** stars, ensuring quality stays.")

    # Deduplicate reasons if needed
    reasons = list(dict.fromkeys(reasons))  # Preserves order, removes duplicates

    return reasons


def generate_recommendations(current_user):
    recommendations = []
    visited_hotels = {b["hotel_id"] for b in current_user["bookings"]}

    for hotel in hotels_data:
        if hotel["hotel_id"] in visited_hotels:
            continue
        if match_user_preferences(current_user, hotel):
            reason_list = generate_reasoning(current_user, hotel)
            recommendations.append({
                "hotel": hotel,
                "reason_list": reason_list
            })

    return recommendations


# -----------------------
# 2.1. COMPONENTS
# -----------------------
def all_hotels_component(current_user):
    st.subheader("All Hotels")
    for hotel in hotels_data:
        with st.expander(f"{hotel['name']} - ${hotel['price_per_night']} / night", expanded=True):
            st.write(f"Location: {get_city_name(hotel['location_id'])}, {get_country_name(hotel['location_id'])}")
            st.write(f"Rating: {hotel['rating']}")
            st.write(f"Amenities: {', '.join(hotel['amenities'])}")
            st.write(f"Themes: {', '.join(hotel['themes'])}")
            associated_events = [
                get_event_by_id(eid)["name"] for eid in hotel["associated_event_ids"] if get_event_by_id(eid)
            ]
            if associated_events:
                st.write(f"Associated Events: {', '.join(associated_events)}")

            if st.button(f"Book {hotel['hotel_id']}", key=f"all_{hotel['hotel_id']}"):
                book_hotel(current_user, hotel["hotel_id"])
                st.rerun()


def recommendations_component(current_user):
    st.subheader("Recommendations")
    recommended_hotels = generate_recommendations(current_user)
    if not recommended_hotels:
        st.write("No specific recommendations at this time. Try booking more or broaden your preferences.")
        return

    for rec in recommended_hotels:
        hotel = rec["hotel"]
        reason_list = rec["reason_list"]
        with st.expander(f"{hotel['name']} - ${hotel['price_per_night']} / night", expanded=True):
            st.write(f"Location: {get_city_name(hotel['location_id'])}, {get_country_name(hotel['location_id'])}")
            st.write(f"Rating: {hotel['rating']}")
            st.write(f"Amenities: {', '.join(hotel['amenities'])}")
            st.write(f"Themes: {', '.join(hotel['themes'])}")
            associated_events = [
                get_event_by_id(eid)["name"] for eid in hotel["associated_event_ids"] if get_event_by_id(eid)
            ]
            if associated_events:
                st.write(f"Associated Events: {', '.join(associated_events)}")

            # Display the reasoning
            st.markdown("**Why we recommend this:**")
            for r in reason_list:
                st.markdown(f"- {r}")

            if st.button(f"Book {hotel['hotel_id']}", key=f"rec_{hotel['hotel_id']}"):
                book_hotel(current_user, hotel["hotel_id"])
                st.rerun()


def past_bookings_component(current_user):
    st.subheader("Your Past Bookings")
    if not current_user["bookings"]:
        st.write("No bookings yet.")
        return

    for b in current_user["bookings"]:
        hotel_info = get_hotel_by_id(b["hotel_id"])
        city_name = get_city_name(b["location_id"])
        country_name = get_country_name(b["location_id"])
        date_booked = b["booking_date"]
        event_info = get_event_by_id(b["event_id"]) if b["event_id"] else None
        event_str = f" (Event: {event_info['name']})" if event_info else ""
        with st.expander(f"Booking ID: {b['booking_id']}", expanded=True):
            st.write(f"**{hotel_info['name']}** in {city_name}, {country_name}, booked on {date_booked}{event_str}")
            st.write(f"Price per night was ${hotel_info['price_per_night']}")
            st.write(f"Amenities: {', '.join(hotel_info['amenities'])}")
            st.write(f"Themes: {', '.join(hotel_info['themes'])}")


# -----------------------
# 2.2. SEARCH PAGE
# -----------------------
def search_hotels_page(current_user):
    st.header("Search and Book a Hotel")
    city_options = sorted({cities_dict[h["location_id"]]["name"] for h in hotels_data})
    selected_city = st.selectbox("Select City", options=["All"] + city_options)

    user_min_price = current_user["preferences"]["preferred_price_range"]["min"]
    user_max_price = current_user["preferences"]["preferred_price_range"]["max"]
    min_price = st.slider("Min Price", 0, 1000, user_min_price)
    max_price = st.slider("Max Price", 0, 1000, user_max_price)

    def city_to_id(name):
        for c in cities_data:
            if c["name"] == name:
                return c["city_id"]
        return None

    filtered_hotels = []
    for hotel in hotels_data:
        if selected_city != "All":
            if city_to_id(selected_city) != hotel["location_id"]:
                continue
        if not (min_price <= hotel["price_per_night"] <= max_price):
            continue
        filtered_hotels.append(hotel)

    if not filtered_hotels:
        st.write("No hotels found for your search. Try adjusting filters.")
    else:
        for fh in filtered_hotels:
            with st.expander(f"{fh['name']} - ${fh['price_per_night']} / night"):
                st.write(f"City: {get_city_name(fh['location_id'])}, {get_country_name(fh['location_id'])}")
                st.write(f"Rating: {fh['rating']}")
                st.write(f"Amenities: {', '.join(fh['amenities'])}")
                st.write(f"Themes: {', '.join(fh['themes'])}")
                associated_events = [
                    get_event_by_id(eid)["name"] for eid in fh["associated_event_ids"] if get_event_by_id(eid)
                ]
                if associated_events:
                    st.write(f"Associated Events: {', '.join(associated_events)}")
                if st.button(f"Book Now ({fh['hotel_id']})", key=f"srch_{fh['hotel_id']}"):
                    book_hotel(current_user, fh["hotel_id"])
                    st.rerun()


# -----------------------
# 2.3. COMBINED VIEW
# -----------------------
def combined_view_page(current_user):
    st.header("Your Personalized Travel Dashboard")
    col1, col2, col3 = st.columns([0.4, 0.4, 0.2], gap="medium")

    with col1:
        all_hotels_component(current_user)

    with col2:
        recommendations_component(current_user)

    with col3:
        past_bookings_component(current_user)


# -----------------------
# 3. LOGIN AND MAIN
# -----------------------
def login_page():
    st.title("AI-Driven Travel Agency Booking Demo")
    st.subheader("Select Your Persona to Log In")

    # Define personas
    personas = {
        "Ahmed Al Reesi": {
            "description": "Tech enthusiast who loves AI and TECH events with moderate budget",
            "user_id": "u1",
            "persona": "Tech Enthusiast"
        },
        "Maryam Al Rasbi": {
            "description": "Luxury seeker interested in culture, spa experiences, and beach.",
            "user_id": "u2",
            "persona": "Luxury Seeker"
        },
        "Mohammad Raza": {
            "description": "Business professional with a penchant for city tours and technology on a mid-to-high budget.",
            "user_id": "u3",
            "persona": "Business Professional"
        }
    }

    persona_names = list(personas.keys())
    selected_persona = st.selectbox(
        "Choose a Persona",
        options=persona_names,
        format_func=lambda name: f"{name} - {personas[name]['description']}"
    )

    if st.button("Login"):
        user_obj = get_user_by_id(personas[selected_persona]["user_id"])
        if user_obj:
            st.session_state["logged_in_user_id"] = user_obj["user_id"]
            st.success(f"Logged in as {user_obj['name']}")
            st.rerun()
        else:
            st.error("Selected persona does not exist.")


def main():
    if "logged_in_user_id" not in st.session_state:
        st.session_state["logged_in_user_id"] = None

    if st.session_state["logged_in_user_id"] is None:
        login_page()
    else:
        current_user_id = st.session_state["logged_in_user_id"]
        current_user = get_user_by_id(current_user_id)
        st.sidebar.title(f"Welcome, {current_user['name']}")

        page_choice = st.sidebar.selectbox(
            "Navigate",
            ["Combined View", "Search Hotels", "Logout"]
        )

        if page_choice == "Combined View":
            combined_view_page(current_user)
        elif page_choice == "Search Hotels":
            search_hotels_page(current_user)
        elif page_choice == "Logout":
            st.session_state["logged_in_user_id"] = None
            st.rerun()


if __name__ == "__main__":
    main()
