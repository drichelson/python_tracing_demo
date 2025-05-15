import aiohttp
import asyncio
import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.resourcedetector.gcp_resource_detector import GoogleCloudResourceDetector
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.instrumentation.aiohttp_client import AioHttpClientInstrumentor

async def main():
    # check if GCP_RESOURCE_DETECTOR is set to true
    if os.getenv("GCP_RESOURCE_DETECTOR").lower() == "true":
        resource = GoogleCloudResourceDetector().detect()
    else:
        resource = Resource.create()

    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter(service_name="test-app")))

    # Set the provider as the global default
    trace.set_tracer_provider(provider)

    AioHttpClientInstrumentor().instrument()

    
    url = "https://www.google.com"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Status: {response.status}")
            html = await response.text()
            print(f"Content length: {len(html)} characters")
            return html


if __name__ == "__main__":
    asyncio.run(main()) 