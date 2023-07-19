package com.shzhangji.demo.flume;

import java.io.ByteArrayInputStream;
import java.util.List;

import org.apache.flume.Context;
import org.apache.flume.Event;
import org.apache.flume.interceptor.Interceptor;
import org.codehaus.jackson.JsonNode;
import org.codehaus.jackson.map.ObjectMapper;

public class ActionTimeInterceptor implements Interceptor {

    private final static ObjectMapper mapper = new ObjectMapper();

    @Override
    public void initialize() {
        // no-op
    }

    @Override
    public Event intercept(Event event) {
        try {
            JsonNode node = mapper.readTree(new ByteArrayInputStream(event.getBody()));
            long timestamp = (long) (node.get("actionTime").getDoubleValue() * 1000);
            event.getHeaders().put("timestamp", Long.toString(timestamp));
        } catch (Exception e) {
            // no-op
        }
        return event;
    }

    @Override
    public List<Event> intercept(List<Event> events) {
        for (Event event : events) {
            intercept(event);
        }
        return events;
    }

    @Override
    public void close() {
        // no-op
    }

    public static class Builder implements Interceptor.Builder {

        @Override
        public void configure(Context context) {
            // no-op
        }

        @Override
        public Interceptor build() {
            return new ActionTimeInterceptor();
        }

    }

}
