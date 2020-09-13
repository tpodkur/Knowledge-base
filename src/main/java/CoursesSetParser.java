import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

class CoursesSetParser {
    void loadCourses(String url, String section) throws InterruptedException {
        WebDriver driver = new ChromeDriver();
        driver.get(url);

        WebDriverWait wait = new WebDriverWait(driver, 60);
        wait.until(new ExpectedCondition<Boolean>() {
            public Boolean apply(WebDriver wdriver) {
                return ((JavascriptExecutor) driver).executeScript(
                        "return document.readyState"
                ).equals("complete");
            }
        });

        TimeUnit.SECONDS.sleep(30);

        WebElement coursePack = driver.findElement(By.className("course-pack"));
        List<WebElement> listItems = coursePack.findElements(By.className("course-pack-list__item"));

        List<Link> courseLinks = new ArrayList<Link>();
        for (WebElement listItem : listItems) {
                WebElement linkElement = listItem.findElement(By.className("ember-link"));
                ((JavascriptExecutor)driver).executeScript("arguments[0].scrollIntoView();", linkElement );
                TimeUnit.SECONDS.sleep(5);
                String link = linkElement.getAttribute("href");
                System.out.println(link);

                Link newLink = new Link(link, section);
                courseLinks.add(newLink);
        }

        CourseParser courseParser = new CourseParser();
        for (Link courseLink : courseLinks) {
            courseParser.loadCourseData(courseLink.getLink(), courseLink.getSection());
        }

        driver.quit();
    }
}