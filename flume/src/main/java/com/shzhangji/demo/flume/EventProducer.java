package com.shzhangji.demo.flume;

import java.io.ByteArrayOutputStream;
import java.nio.ByteBuffer;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

import org.apache.avro.io.BinaryEncoder;
import org.apache.avro.io.EncoderFactory;
import org.apache.avro.specific.SpecificDatumWriter;
import org.apache.flume.source.avro.AvroFlumeEvent;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;

public class EventProducer {

    public void produce() throws Exception {
        Map<CharSequence, CharSequence> headers = new HashMap<>();
        headers.put("timestamp", "1498525680023");
        String body = "some message";
        AvroFlumeEvent event = new AvroFlumeEvent(headers, ByteBuffer.wrap(body.getBytes()));

        ByteArrayOutputStream out = new ByteArrayOutputStream();
        BinaryEncoder encoder = EncoderFactory.get().directBinaryEncoder(out, null);
        SpecificDatumWriter<AvroFlumeEvent> writer = new SpecificDatumWriter<>(AvroFlumeEvent.class);
        writer.write(event, encoder);
        encoder.flush();

        Properties props = new Properties();
        Producer<String, byte[]> producer = new KafkaProducer<>(props);
        producer.send(new ProducerRecord<String, byte[]>("alog", out.toByteArray()));
        producer.close();
    }

}
