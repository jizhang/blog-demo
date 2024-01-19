from collections.abc import Sized, Iterable, Iterator


class Bucket(Sized, Iterable[int]):
    def __len__(self) -> int:
        return 0

    def __iter__(self) -> Iterator[int]:
        return iter([])

bucket: Iterable[int] = Bucket()


class DuckBucket:
    def __len__(self) -> int:
        return 0

    def __iter__(self) -> Iterator[int]:
        return iter([])

duck_bucket: Iterable[int] = DuckBucket()
