from typing import Protocol

from schema import CalendarEventRequest, CalendarsRequest, CalendarsResponse


class CalendarService(Protocol):
    def calendarList(self) -> "CalendarList": ...

    def events(self) -> "Events": ...

    def calendars(self) -> "Calendars": ...


class CalendarList(Protocol):
    def list(self) -> "SessionObject": ...


class SessionObject(Protocol):
    def execute(self) -> dict: ...


class Events(Protocol):
    def list(
        self,
        calendarId: str,
        timeMin: str,
        maxResults: int,
        singleEvents: bool,
        orderBy: str,
    ) -> "SessionObject": ...
    def insert(self, calendarId: str, body: CalendarEventRequest) -> SessionObject: ...
    def update(self, calendarId: str, eventId: str, body: CalendarEventRequest) -> SessionObject: ...
    def delete(self, calendarId: str, eventId: str) -> SessionObject: ...


class Calendars(Protocol):
    def get(self, calendarId: str) -> "SessionObject": ...
    def delete(self, calendarId: str) -> "SessionObject": ...
    def insert(self, body: CalendarsRequest): ...
    def update(self, calendarId: str, body: CalendarsRequest) -> CalendarsResponse: ...
