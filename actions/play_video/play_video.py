from pathlib import Path

from gi.repository import Adw, Gtk, Pango
from GtkHelper.GtkHelper import ComboRow, ScaleRow
from urllib.parse import urlparse, parse_qs

from ..playlist_action_base import YoutubePlaylistBase


class PlayVideoAction(YoutubePlaylistBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def url(self) -> str:
        return self._get_property(key="url", default=100, enforce_type=float)

    @url.setter
    def url(self, value: str):
        self._set_property(key="url", value=value)

    def _playlist_hash(self, url: str) -> str | None:
        url = self.url
        if not url:
            return None

        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        l = params.get("list")
        if l:
            return l[0]

        return None

    def _video_hash(self, url: str) -> str | None:
        url = self.url
        if not url:
            return None

        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        v = params.get("v")
        if v:
            return v[0]

        return None

    @property
    def playlist_hash(self) -> str | None:
        return self._playlist_hash(url=self.url)

    def _is_playlist(self, url: str) -> bool:
        return bool(self._playlist_hash(url=url))
