from raven import Client

client = Client('https://8a884d6b0f7d40bcb3bca3fc746cf9b2:94ea70c88887490db7cdc56503368f0c@sentry.io/1276997')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()
end
