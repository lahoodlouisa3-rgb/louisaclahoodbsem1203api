import asyncio
from typing import Dict


class BookStore:
    def __init__(self) -> None:
        self.inventory: Dict[str, bool] = {"math_book": True}
        self.mutex = asyncio.Lock()

    async def checkout(self, name: str, item: str) -> None:
        print(f"{name} attempts to get {item}")
        await asyncio.sleep(3)

        async with self.mutex:
            if self.inventory.get(item, False):
                self.inventory[item] = False
                print(f"{name} obtained {item}")
            else:
                print(f"{item} cannot be taken by {name}")

    async def checkin(self, name: str, item: str) -> None:
        print(f"{name} submits {item}")
        await asyncio.sleep(5)

        async with self.mutex:
            self.inventory[item] = True
            print(f"{name} successful return of {item}")


async def execute_flow(store: BookStore) -> None:
    await asyncio.gather(
        store.checkout("Thiago", "english_book"),
        store.checkout("Mavin", "english_book"),
        store.checkin("Thiago", "english_book"),
        store.checkout("Vanessa", "english_book"),
    )


def launch() -> None:
    store = BookStore()
    asyncio.run(execute_flow(store))


if __name__ == "__main__":
    launch()