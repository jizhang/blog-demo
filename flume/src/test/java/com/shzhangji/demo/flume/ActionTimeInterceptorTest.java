package com.shzhangji.demo.flume;

import java.nio.charset.StandardCharsets;
import java.util.Collections;

import com.shzhangji.demo.flume.ActionTimeInterceptor;
import org.apache.flume.Event;
import org.apache.flume.event.EventBuilder;
import org.apache.flume.interceptor.Interceptor;
import org.junit.Assert;
import org.junit.Test;


public class ActionTimeInterceptorTest {

    @Test
    public void testIntercept() {
        Interceptor interceptor = new ActionTimeInterceptor.Builder().build();
        Event event = EventBuilder.withBody("{\"actionTime\":1498525680.023}",
                StandardCharsets.UTF_8, Collections.emptyMap());
        String timestamp = interceptor.intercept(event).getHeaders().get("timestamp");
        Assert.assertEquals("1498525680023", timestamp);
    }

}
