from prefect import flow, serve


@flow
def main():
    print("Hello from test-prefect!")


if __name__ == "__main__":
    if __name__ == "__main__":
        hello = Deployment.build_from_flow(
            flow=main,
            name="test-prefect",
            tags=["test"],
            schedule=CronSchedule(cron="0 0 * * *"),  # ✅ Указываем без `parameters`
        )

        hello.apply()  # ✅ Отправляет деплой напрямую на Prefect Server
