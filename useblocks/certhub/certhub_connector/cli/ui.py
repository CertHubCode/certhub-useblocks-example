"""Rich-based terminal UI for cadence (styling only — no business logic)."""

from __future__ import annotations

import os
import sys

from rich.console import Console, Group
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

# Customer-facing product line for the Cadence showcase.
_PRODUCT_LINE = "Cadence · SaMD Engineering Loop"
_WORDMARK = Text.from_markup(
    f"[bold cyan]CERTHUB[/bold cyan]\n[dim]{_PRODUCT_LINE}[/dim]"
)


def is_plain() -> bool:
    """True when logos/colors should be suppressed (CI / NO_COLOR / non-TTY)."""
    if os.environ.get("NO_COLOR", "").strip():
        return True
    if os.environ.get("CI", "").strip():
        return True
    return not sys.stdout.isatty()


def console(*, stderr: bool = False) -> Console:
    """Shared Console; forces plain markup when ``is_plain()``."""
    plain = is_plain()
    return Console(
        stderr=stderr,
        no_color=plain,
        force_terminal=False if plain else None,
        highlight=False,
    )


def banner(command: str) -> None:
    """Print CertHub wordmark + command title."""
    if not command or not command.strip():
        raise ValueError("Missing required field: 'command'")
    out = console()
    title = command.strip()
    if is_plain():
        out.print(f"CertHub — {title}")
        out.print("")
        return
    out.print(
        Panel(
            _WORDMARK,
            title="[bold]CertHub[/bold]",
            subtitle=f"[dim]{title}[/dim]",
            border_style="cyan",
            padding=(0, 2),
        )
    )
    out.print("")


def step(title: str) -> None:
    if not title or not title.strip():
        raise ValueError("Missing required field: 'title'")
    out = console()
    if is_plain():
        out.print(f"── {title.strip()} ──")
        return
    out.print(Rule(title.strip(), style="cyan"))


def ok(msg: str) -> None:
    console().print(f"[green]✓[/green] {msg}" if not is_plain() else f"OK: {msg}")


def warn(msg: str) -> None:
    console().print(
        f"[yellow]![/yellow] {msg}" if not is_plain() else f"WARNING: {msg}"
    )


def fail(msg: str) -> None:
    console(stderr=True).print(
        f"[red]✗[/red] {msg}" if not is_plain() else f"ERROR: {msg}"
    )


def details(rows: list[tuple[str, str]], *, title: str | None = None) -> None:
    """Render a two-column details table (label / value)."""
    if not rows:
        raise ValueError("Missing required field: 'rows'")
    for label, _value in rows:
        if not label or not label.strip():
            raise ValueError("Missing required field: 'label'")
    out = console()
    if is_plain():
        if title and title.strip():
            out.print(title.strip())
        for label, value in rows:
            out.print(f"  {label.strip()}: {value}")
        return
    table = Table(
        show_header=False,
        box=None,
        padding=(0, 2),
        expand=False,
    )
    table.add_column(style="dim", no_wrap=True)
    table.add_column(overflow="fold")
    for label, value in rows:
        table.add_row(label.strip(), str(value))
    if title and title.strip():
        out.print(
            Panel(table, title=f"[bold]{title.strip()}[/bold]", border_style="cyan")
        )
    else:
        out.print(table)


def link_panel(title: str, url: str, *, note: str | None = None) -> None:
    if not title or not title.strip():
        raise ValueError("Missing required field: 'title'")
    if not url or not url.strip():
        raise ValueError("Missing required field: 'url'")
    if is_plain():
        print(f"{title.strip()}: {url.strip()}", flush=True)
        if note and note.strip():
            print(f"  {note.strip()}", flush=True)
        return
    body: Text | Group
    if note and note.strip():
        body = Group(
            Text.from_markup(f"[link={url.strip()}]{url.strip()}[/link]"),
            Text.from_markup(f"\n[dim]{note.strip()}[/dim]"),
        )
    else:
        body = Text.from_markup(f"[link={url.strip()}]{url.strip()}[/link]")
    console().print(
        Panel(
            body,
            title=f"[bold]{title.strip()}[/bold]",
            border_style="green",
            padding=(0, 1),
        )
    )


def success_panel(title: str, rows: list[tuple[str, str]]) -> None:
    """Highlight a completed action with key facts."""
    if not title or not title.strip():
        raise ValueError("Missing required field: 'title'")
    if not rows:
        raise ValueError("Missing required field: 'rows'")
    out = console()
    if is_plain():
        out.print(f"OK: {title.strip()}")
        for label, value in rows:
            out.print(f"  {label.strip()}: {value}")
        return
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column(style="dim", no_wrap=True)
    table.add_column()
    for label, value in rows:
        table.add_row(label.strip(), str(value))
    out.print(
        Panel(
            table,
            title=f"[bold green]✓ {title.strip()}[/bold green]",
            border_style="green",
            padding=(0, 1),
        )
    )
