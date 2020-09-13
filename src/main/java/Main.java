import java.util.ArrayList;
import java.util.List;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.util.concurrent.TimeUnit;
import java.util.Date;


public class Main {
    public static void main(String[] args) throws InterruptedException {
        String url = "https://stepik.org/catalog?tag=866";
        CoursesSetParser setParser = new CoursesSetParser();
        setParser.loadCourses(url, "section");
    }

    public void parser() throws InterruptedException {
        String url = "https://stepik.org/catalog";
        System.setProperty("webdriver.chrome.driver", "/usr/local/bin/chromedriver");
        WebDriver driver = new ChromeDriver();

//        driver.manage().timeouts().implicitlyWait(240, TimeUnit.SECONDS);
        driver.get(url);

//        WebDriverWait wait = new WebDriverWait(driver, 60);
//        wait.until(new ExpectedCondition<Boolean>() {
//            public Boolean apply(WebDriver wdriver) {
//                return ((JavascriptExecutor) driver).executeScript(
//                        "return document.readyState"
//                ).equals("complete");
//            }
//        });
        TimeUnit.SECONDS.sleep(30);

        List<WebElement> courseSets = driver
                .findElement(By.className("st-course-filters"))
                .findElements(By.className("st-filter"));

        List<Link> courseLinks = new ArrayList<Link>();
        for (WebElement courseSet : courseSets) {
            List<WebElement> listItems = courseSet.findElements(By.className("st-filter__item"));
            for (WebElement listItem : listItems) {
                WebElement linkElement = listItem.findElement(By.className("st-filter__link"));
                String link = linkElement.getAttribute("href");
                String section = linkElement.getText();

                Link newLink = new Link(link, section);
                courseLinks.add(newLink);
            }
        }

        CoursesSetParser setParser = new CoursesSetParser();
        for (Link courseLink : courseLinks) {
            setParser.loadCourses(courseLink.getLink(), courseLink.getSection());
        }

        driver.quit();
    }
}
