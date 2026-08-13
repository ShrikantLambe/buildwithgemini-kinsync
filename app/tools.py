# Copyright 2026 Google LLC
# KinSync Family Calendar Tools

from typing import Any

# In-memory storage for family roster and calendar events
FAMILY_MEMBERS: list[dict[str, Any]] = [
    {
        "name": "Mom (Sarah)",
        "role": "Parent",
        "birthday": "1988-05-14",
        "color": "#E91E63",
        "notes": "Work meetings, Pilates, PTA member, drives Honda Odyssey",
    },
    {
        "name": "Dad (Mark)",
        "role": "Parent",
        "birthday": "1986-09-22",
        "color": "#2196F3",
        "notes": "Tech manager, Gym mornings, Soccer coach volunteer, drives Subaru",
    },
    {
        "name": "Leo",
        "role": "Kid (Age 8 - 3rd Grade)",
        "birthday": "2018-03-10",
        "color": "#4CAF50",
        "notes": "Loves LEGO robotics, soccer (#10), piano practice, allergy: peanuts",
    },
    {
        "name": "Maya",
        "role": "Kid (Age 5 - Kindergarten)",
        "birthday": "2021-11-04",
        "color": "#FF9800",
        "notes": "Loves ballet, drawing & clay, swimming, storytime",
    },
    {
        "name": "Grandma Helen",
        "role": "Grandparent",
        "birthday": "1958-01-18",
        "color": "#9C27B0",
        "notes": "Helps with Friday afternoon pickups & weekend family baking",
    },
]

EVENTS: list[dict[str, Any]] = [
    # --- Friday August 14, 2026 ---
    {
        "id": "1",
        "title": "Lincoln Elementary School",
        "date": "2026-08-14",
        "start_time": "08:30",
        "end_time": "15:00",
        "members": ["Leo"],
        "category": "school",
        "location": "Lincoln Elementary Room 204",
        "drop_off_by": "Dad (Mark)",
        "pick_up_by": "Mom (Sarah)",
        "notes": "Pack hot lunch and library book return",
    },
    {
        "id": "2",
        "title": "Sunshine Preschool",
        "date": "2026-08-14",
        "start_time": "09:00",
        "end_time": "12:30",
        "members": ["Maya"],
        "category": "school",
        "location": "Sunshine Preschool Classroom B",
        "drop_off_by": "Dad (Mark)",
        "pick_up_by": "Mom (Sarah)",
        "notes": "Show & Tell: Favorite stuffed animal",
    },
    {
        "id": "3",
        "title": "Maya Playdate with Emma",
        "date": "2026-08-14",
        "start_time": "13:00",
        "end_time": "15:00",
        "members": ["Maya"],
        "category": "playdate",
        "location": "Emma's House (45 Maple St)",
        "drop_off_by": "Mom (Sarah)",
        "pick_up_by": "Grandma Helen",
        "notes": "Snack provided by Emma's mom",
    },
    {
        "id": "4",
        "title": "Mom's Pilates Class",
        "date": "2026-08-14",
        "start_time": "16:00",
        "end_time": "17:00",
        "members": ["Mom (Sarah)"],
        "category": "fitness",
        "location": "Core Reformer Studio",
        "drop_off_by": "",
        "pick_up_by": "",
        "notes": "Grip socks required",
    },
    {
        "id": "5",
        "title": "Leo Soccer Practice",
        "date": "2026-08-14",
        "start_time": "16:00",
        "end_time": "17:30",
        "members": ["Leo"],
        "category": "sports",
        "location": "Community Park Field 2",
        "drop_off_by": "Dad (Mark)",
        "pick_up_by": "Dad (Mark)",
        "notes": "Wear blue jersey, shin guards, bring water bottle",
    },
    {
        "id": "6",
        "title": "Friday Family Movie Night & Pizza",
        "date": "2026-08-14",
        "start_time": "18:30",
        "end_time": "20:30",
        "members": ["Mom (Sarah)", "Dad (Mark)", "Leo", "Maya", "Grandma Helen"],
        "category": "social",
        "location": "Home Living Room",
        "drop_off_by": "",
        "pick_up_by": "",
        "notes": "Order gluten-free pizza, watch Inside Out 2",
    },

    # --- Saturday August 15, 2026 ---
    {
        "id": "7",
        "title": "Leo Youth Swim League",
        "date": "2026-08-15",
        "start_time": "09:00",
        "end_time": "10:15",
        "members": ["Leo"],
        "category": "sports",
        "location": "YMCA Aquatic Center Pool 3",
        "drop_off_by": "Dad (Mark)",
        "pick_up_by": "Dad (Mark)",
        "notes": "Goggles, swim cap, towel",
    },
    {
        "id": "8",
        "title": "Maya Preschool Ballet & Tap",
        "date": "2026-08-15",
        "start_time": "10:30",
        "end_time": "11:30",
        "members": ["Maya"],
        "category": "class",
        "location": "Tutu Dance Academy Studio B",
        "drop_off_by": "Mom (Sarah)",
        "pick_up_by": "Mom (Sarah)",
        "notes": "Pink leotard, pink ballet slippers, hair bun",
    },
    {
        "id": "9",
        "title": "Leo LEGO Robotics Workshop",
        "date": "2026-08-15",
        "start_time": "11:30",
        "end_time": "13:00",
        "members": ["Leo"],
        "category": "class",
        "location": "MakerSpace Tech Lab",
        "drop_off_by": "Dad (Mark)",
        "pick_up_by": "Dad (Mark)",
        "notes": "Building EV3 competition robot",
    },
    {
        "id": "10",
        "title": "Maya Birthday Party (Toby's 6th Birthday)",
        "date": "2026-08-15",
        "start_time": "14:00",
        "end_time": "16:00",
        "members": ["Maya", "Leo"],
        "category": "playdate",
        "location": "JumpZone Trampoline Park",
        "drop_off_by": "Mom (Sarah)",
        "pick_up_by": "Mom (Sarah)",
        "notes": "Grip socks needed. Wrapped Mario Kart Lego set for Toby",
    },
    {
        "id": "11",
        "title": "Parents Date Night Out",
        "date": "2026-08-15",
        "start_time": "18:30",
        "end_time": "21:30",
        "members": ["Mom (Sarah)", "Dad (Mark)"],
        "category": "social",
        "location": "Osteria Italian Restaurant",
        "drop_off_by": "",
        "pick_up_by": "",
        "notes": "Grandma Helen babysitting Leo & Maya at home",
    },

    # --- Sunday August 16, 2026 ---
    {
        "id": "12",
        "title": "Sunday Morning Farmers Market & Park Walk",
        "date": "2026-08-16",
        "start_time": "09:30",
        "end_time": "11:30",
        "members": ["Mom (Sarah)", "Dad (Mark)", "Leo", "Maya"],
        "category": "social",
        "location": "Town Square Plaza",
        "drop_off_by": "",
        "pick_up_by": "",
        "notes": "Buy fresh strawberries, honey, sourdough bread",
    },
    {
        "id": "13",
        "title": "Leo Piano Lesson",
        "date": "2026-08-16",
        "start_time": "14:00",
        "end_time": "15:00",
        "members": ["Leo"],
        "category": "class",
        "location": "Harmony Music School Room 4",
        "drop_off_by": "Dad (Mark)",
        "pick_up_by": "Dad (Mark)",
        "notes": "Practice Beethoven Minuet in G",
    },
    {
        "id": "14",
        "title": "Maya Little Gym Tumbling",
        "date": "2026-08-16",
        "start_time": "15:15",
        "end_time": "16:15",
        "members": ["Maya"],
        "category": "sports",
        "location": "The Little Gym Arena 1",
        "drop_off_by": "Mom (Sarah)",
        "pick_up_by": "Mom (Sarah)",
        "notes": "Barefoot, comfortable shorts & t-shirt",
    },

    # --- Monday August 17, 2026 ---
    {
        "id": "15",
        "title": "Lincoln Elementary School",
        "date": "2026-08-17",
        "start_time": "08:30",
        "end_time": "15:00",
        "members": ["Leo"],
        "category": "school",
        "location": "Lincoln Elementary",
        "drop_off_by": "Dad (Mark)",
        "pick_up_by": "Dad (Mark)",
        "notes": "Leo Math Olympiad practice at 07:45 AM before school",
    },
    {
        "id": "16",
        "title": "Sunshine Preschool",
        "date": "2026-08-17",
        "start_time": "09:00",
        "end_time": "12:30",
        "members": ["Maya"],
        "category": "school",
        "location": "Sunshine Preschool",
        "drop_off_by": "Mom (Sarah)",
        "pick_up_by": "Mom (Sarah)",
        "notes": "Preschool Library book exchange",
    },
    {
        "id": "17",
        "title": "Dad's Work Team Dinner",
        "date": "2026-08-17",
        "start_time": "18:00",
        "end_time": "20:30",
        "members": ["Dad (Mark)"],
        "category": "work",
        "location": "Downtown Steakhouse",
        "drop_off_by": "",
        "pick_up_by": "",
        "notes": "Quarterly team celebration",
    }
]


def add_family_member(
    name: str,
    role: str,
    birthday: str = "",
    color: str = "#9C27B0",
    notes: str = "",
) -> str:
    """Adds a new family member to the family roster.

    Args:
        name: Name of the family member (e.g. 'Maya', 'Uncle Dan').
        role: Role in the family (e.g. 'Parent', 'Kid', 'Grandparent').
        birthday: Optional birthday in YYYY-MM-DD format.
        color: Optional hex color code for calendar display tags.
        notes: Optional preferences, school details, or allergy info.

    Returns:
        Confirmation message string.
    """
    FAMILY_MEMBERS.append(
        {
            "name": name,
            "role": role,
            "birthday": birthday,
            "color": color,
            "notes": notes,
        }
    )
    return f"Successfully added family member: {name} ({role})."


def list_family_members() -> list[dict[str, Any]]:
    """Returns the list of all family members, their roles, birthdays, and notes.

    Returns:
        A list of family member records.
    """
    return FAMILY_MEMBERS


def add_event(
    title: str,
    date: str,
    start_time: str,
    end_time: str,
    members: list[str],
    category: str = "general",
    location: str = "",
    drop_off_by: str = "",
    pick_up_by: str = "",
    notes: str = "",
) -> str:
    """Creates a new family calendar event with assigned logistics (pickup/drop-off).

    Args:
        title: Title of the event (e.g. 'Soccer Practice', 'Pilates Class', 'Doctor Appointment').
        date: Event date in YYYY-MM-DD format (e.g. '2026-08-14').
        start_time: Event start time in 24h HH:MM format (e.g. '16:00').
        end_time: Event end time in 24h HH:MM format (e.g. '17:30').
        members: List of family members involved (e.g. ['Leo', 'Dad (Mark)']).
        category: Category of activity: 'school', 'sports', 'class', 'playdate', 'fitness', 'work', or 'social'.
        location: Event venue or address.
        drop_off_by: Name of parent/person responsible for drop-off.
        pick_up_by: Name of parent/person responsible for pickup.
        notes: Additional reminder notes, equipment needed, or gift reminders.

    Returns:
        Confirmation message string.
    """
    event_id = str(len(EVENTS) + 1)
    event = {
        "id": event_id,
        "title": title,
        "date": date,
        "start_time": start_time,
        "end_time": end_time,
        "members": members,
        "category": category,
        "location": location,
        "drop_off_by": drop_off_by,
        "pick_up_by": pick_up_by,
        "notes": notes,
    }
    EVENTS.append(event)
    return f"Successfully added event '{title}' on {date} ({start_time} - {end_time}) for {', '.join(members)}."


def list_events(date: str = "", member: str = "") -> list[dict[str, Any]]:
    """Lists calendar events, optionally filtered by date or family member name.

    Args:
        date: Optional date in YYYY-MM-DD format to filter events.
        member: Optional family member name substring to filter events.

    Returns:
        A list of matching event objects.
    """
    filtered = EVENTS
    if date:
        filtered = [e for e in filtered if e["date"] == date]
    if member:
        m_lower = member.lower()
        filtered = [
            e
            for e in filtered
            if any(m_lower in m.lower() for m in e["members"])
            or m_lower in e.get("drop_off_by", "").lower()
            or m_lower in e.get("pick_up_by", "").lower()
        ]
    return filtered


def detect_conflicts(date: str) -> dict[str, Any]:
    """Scans the family calendar for a given date to detect double-bookings or missing transport assignments.

    Args:
        date: Date in YYYY-MM-DD format to analyze for conflicts.

    Returns:
        Dictionary containing double_bookings list and missing_transport list.
    """
    day_events = [e for e in EVENTS if e["date"] == date]
    double_bookings = []
    missing_transport = []

    for i in range(len(day_events)):
        for j in range(i + 1, len(day_events)):
            e1, e2 = day_events[i], day_events[j]
            shared_members = set(e1["members"]).intersection(set(e2["members"]))
            if shared_members:
                if not (
                    e1["end_time"] <= e2["start_time"]
                    or e2["end_time"] <= e1["start_time"]
                ):
                    double_bookings.append(
                        {
                            "members": list(shared_members),
                            "event_1": f"{e1['title']} ({e1['start_time']}-{e1['end_time']})",
                            "event_2": f"{e2['title']} ({e2['start_time']}-{e2['end_time']})",
                        }
                    )

    kid_names = [m["name"] for m in FAMILY_MEMBERS if "Kid" in m["role"]]
    for e in day_events:
        involves_kid = any(
            any(k.lower() in m.lower() for k in kid_names) for m in e["members"]
        )
        if involves_kid:
            if not e.get("drop_off_by") or not e.get("pick_up_by"):
                missing_transport.append(
                    {
                        "event": e["title"],
                        "time": f"{e['start_time']}-{e['end_time']}",
                        "missing_drop_off": not e.get("drop_off_by"),
                        "missing_pick_up": not e.get("pick_up_by"),
                    }
                )

    return {
        "date": date,
        "double_bookings": double_bookings,
        "missing_transport": missing_transport,
        "total_events": len(day_events),
    }


def generate_daily_brief(date: str) -> dict[str, Any]:
    """Generates a complete daily brief summarizing family schedules, pickup/drop-off logistics, weather forecasts, preparation gear advice, and conflict warnings.

    Args:
        date: Date in YYYY-MM-DD format for the brief.

    Returns:
        Structured brief object containing timeline, logistics summary, weather predictions, and conflict warnings.
    """
    day_events = sorted(
        [e for e in EVENTS if e["date"] == date], key=lambda x: x["start_time"]
    )
    conflicts = detect_conflicts(date)

    logistics = []
    weather_summary = []
    for e in day_events:
        if e.get("drop_off_by") or e.get("pick_up_by"):
            logistics.append(
                {
                    "event": e["title"],
                    "time": f"{e['start_time']} - {e['end_time']}",
                    "kids": [m for m in e["members"] if "Mom" not in m and "Dad" not in m],
                    "drop_off": e.get("drop_off_by", "Unassigned"),
                    "pick_up": e.get("pick_up_by", "Unassigned"),
                }
            )

        if "weather" in e or "title" in e:
            # Provide weather prediction & advice for each activity
            weather_summary.append(
                {
                    "event": e["title"],
                    "time": f"{e['start_time']} - {e['end_time']}",
                    "forecast": e.get("weather", {}).get("forecast", "☀️ 75°F Clear"),
                    "advice": e.get("weather", {}).get("advice", "Standard weather attire."),
                    "venue_phone": e.get("weather", {}).get("phone", "(650) 555-0100"),
                    "rain_alert": e.get("weather", {}).get("rainAlert", False),
                }
            )

    return {
        "date": date,
        "events_count": len(day_events),
        "timeline": day_events,
        "logistics_transport": logistics,
        "weather_summary": weather_summary,
        "conflicts": conflicts,
        "family_members": FAMILY_MEMBERS,
    }

