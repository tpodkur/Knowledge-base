import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.concurrent.TimeUnit;


class CourseParser {
    void loadCourseData(String url, String section) throws InterruptedException {
        WebDriver driver = new ChromeDriver();
        driver.get(url);
        TimeUnit.SECONDS.sleep(10);

        WebElement title = driver.findElement(By.className("course-promo__header"));
        WebElement description = driver.findElement(By.className("shortened-text"));
        WebElement cost = driver.findElement(By.className("course-promo-enrollment__price"));
        Integer intCost = (cost.getText().equals("Бесплатно")) ? 0 : Integer.parseInt(cost.getText());
        Course course = new Course(title.getText(), description.getText(), intCost, section);

        System.out.println(course.getTitle());
        System.out.println(course.getSection());
        System.out.println(course.getDescription());
        System.out.println(course.getCost());

        driver.quit();
    }
}
