from typing import Protocol
from collections.abc import Iterable


class Closeable(Protocol):
    def close(self) -> None: ...


class Resource:
    def close(self):
        self.file.close()


def close_all(resources: Iterable[Closeable]):
    for r in resources:
        r.close()


r1 = Resource()
r2 = Resource()
close_all([r1, r2])
