import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaProducer;
import org.apache.flink.streaming.util.serialization.SimpleStringSchema;

public class RedditTrendAnalysis {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        env.addSource(new FlinkKafkaConsumer<>("reddit-posts", new SimpleStringSchema(), properties))
           .map(value -> new Gson().fromJson(value, RedditPost.class))
           .keyBy("subreddit")
           .timeWindow(Time.minutes(5))
           .sum("score")
           .addSink(new FlinkKafkaProducer<>("reddit-trends", new SimpleStringSchema(), properties));
        env.execute("Reddit Trend Analysis");
    }
}