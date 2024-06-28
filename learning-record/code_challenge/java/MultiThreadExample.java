import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class MultiThreadExample {

    public static void main(String[] args) {
        int numThreads = 5;
        CountDownLatch latch = new CountDownLatch(numThreads);
        ExecutorService executor = Executors.newFixedThreadPool(numThreads);

        for (int i = 0; i < numThreads; i++) {
            int threadNumber = i + 1;
            executor.execute(() -> {
                try {
                    // Simulate some work with a sleep
                    System.out.println("Thread " + threadNumber + " is working...");
                    Thread.sleep((long) (Math.random() * 1000));
                    System.out.println("Thread " + threadNumber + " has finished.");
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                } finally {
                    latch.countDown(); // Decrement the count of the latch
                }
            });
        }

        try {
            latch.await(); // Wait for all threads to finish
            System.out.println("All threads have finished.");
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            executor.shutdown(); // Shutdown the executor
        }
    }
}
