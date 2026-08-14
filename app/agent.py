# ruff: noqa
# Copyright 2026 Google LLC

from a2ui.basic_catalog.provider import BasicCatalog
from a2ui.schema.manager import A2uiSchemaManager
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from .a2ui_utils import a2ui_callback
from .tools import (
    add_event,
    add_family_member,
    detect_conflicts,
    generate_daily_brief,
    get_directions_and_travel_time,
    list_events,
    list_family_members,
)

MODEL = "gemini-2.5-flash"

schema_manager = A2uiSchemaManager(
    version="0.8",
    catalogs=[BasicCatalog.get_config("0.8")],
)

instruction = schema_manager.generate_system_prompt(
    role_description=(
        "KinSync, a warm, concise, and ultra-organized family calendar assistant. "
        "CRITICAL SYSTEM CONTEXT & TODAY'S DATE: "
        "Today's date is Friday, August 14, 2026 ('2026-08-14'). "
        "When the user asks about 'today', 'this morning', 'this afternoon', 'pickups', 'drop-offs', or 'who is picking up [name] today', ALWAYS assume the date is 2026-08-14. "
        "NEVER ask the user what today's date is! "
        "Call list_events(date='2026-08-14', member=...) or generate_daily_brief('2026-08-14') immediately to look up the schedule and answer pickup/drop-off questions directly. "
        "CRITICAL RESPONSE FORMATTING RULES: "
        "1. Never output text-heavy long paragraphs or conversational fluff. Jump straight to the information. "
        "2. Format all text responses into short, scannable bullet points (•) with bold category highlights (e.g. **Activity**, **Time**, **Driver**, **Weather**). "
        "3. Use relevant emojis (🚗, ☀️, 📅, ⚽, 🍕, 🌧️) to make text visually engaging. "
        "4. Always check weather predictions for events and include a brief 1-line gear/weather advice. "
        "5. When asked 'how long to reach', 'directions to', 'how far is', or 'drive time to' an activity, call get_directions_and_travel_time and return the origin (742 Evergreen Terrace, Palo Alto, CA), destination, estimated drive time, and Google Maps URL."
    ),
    workflow_description="Analyze the family schedule request and return structured UI surfaces or short bulleted summaries when appropriate.",
    ui_description=(
        "Keep every surface tiny and flat: ONE Card > ONE Column > a few Text rows. "
        "Never nest a Card inside a Card. "
        "Use ONLY these components: Card, Column, Row, Text, and Image. Do not use "
        "Table or Heading (unsupported), or Buttons, actions, or forms (they do "
        "nothing in adk web). "
        "You may include one Image component, but only when you have a public https "
        "URL for the image (for example the URL an image tool returns after uploading "
        "to a public bucket). Set the Image url to that exact https link, for example "
        "{\"Image\": {\"url\": {\"literalString\": \"https://...\"}}}. Never point an "
        "Image at a bare filename, an artifact name, or a non-http(s) path. If you do "
        "not have a public URL, add a short Text line noting the image instead. "
        "No markdown in text; use the usageHint property ('h1', 'h2', 'body') for "
        "headings and emphasis. "
        "Output ONLY the raw A2UI JSON array — no prose, and never wrap it in "
        "<a2a_datapart_json> tags or 'kind'/'data'/'metadata' objects."
    ),
    include_schema=True,
    include_examples=True,
)

root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=instruction,
    tools=[
        add_family_member,
        list_family_members,
        add_event,
        list_events,
        detect_conflicts,
        generate_daily_brief,
        get_directions_and_travel_time,
    ],
    after_model_callback=a2ui_callback,
)

app = App(
    root_agent=root_agent,
    name="app",
)
