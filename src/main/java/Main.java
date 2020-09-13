import com.github.igorsuhorukov.phantomjs.PhantomJsDowloader;
import jodd.io.NetUtil;
import jodd.util.SystemUtil;
import org.jsoup.*;
import org.jsoup.select.*;
import org.jsoup.nodes.*;

import java.io.*;
import java.net.URL;

import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.HtmlPage;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {

//        try {
//            WebClient client = new WebClient();
//            HtmlPage page = client.getPage("https://stepik.org/catalog");
//
//            System.out.println(page);
//        } catch (IOException e) {
//            System.out.println("1");
//        }
//
//        try {
//            File file = new File("google.html");
//            NetUtil.downloadFile("https://stepik.org/catalog", file);
//
//            System.out.println(file);
//        } catch (IOException e) {
//
//        }


//        try {
//            URL u = new URL("https://stepik.org/catalog");
//            InputStream in = u.openStream();
//            BufferedReader reader = new BufferedReader(new InputStreamReader(in));
//            StringBuilder result = new StringBuilder();
//            String line;
//            while((line = reader.readLine()) != null) {
//                result.append(line);
//            }
//            System.out.println(result.toString());
//        }catch (IOException e) {
//
//        }

        try {
            Document doc = Jsoup.connect("https://stepik.org/catalog")
                    .userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
                    .get();
            String text = doc.body().html();
            String html = doc.outerHtml();
            System.out.println(html);

//            Element main = doc.getElementsByTag("main").first();
//            Element section = main.getElementsByTag("section").first();
//            Elements ols = section.getElementsByClass("course-pack ember-view");
//
//            Element firstOl = ols.first();
//            Elements refers = firstOl.getElementsByTag("a");
//            for (Element link : refers) {
//                String linkHref = link.attr("href");
//                System.out.println(linkHref);
//            }

        } catch (IOException e) {
        }

        String phantomJsPath = PhantomJsDowloader.getPhantomJsPath();
        WebDriver driver = new PhantomJSDriver(settings)
    }
}

//import com.gargoylesoftware.htmlunit.WebClient;
//import com.gargoylesoftware.htmlunit.html.HtmlPage;
//import java.io.IOException;
//
//        try {
//            WebClient client = new WebClient();
//            HtmlPage page = client.getPage("https://newyork.craigslist.org/search/sss?sort=rel&query=iphone+6s");
//
//            System.out.println(page);
//        } catch (IOException e) {
//            System.out.println("1");
//        }


//import org.jsoup.*;
//import org.jsoup.select.*;
//import org.jsoup.nodes.*;
//import java.io.IOException;

//        try {
//            Document doc = Jsoup.connect("https://stepik.org/catalog?verb").get();
//            String text = doc.body().html();
//            String html = doc.outerHtml();
//            System.out.println(html);
//
//            Element main = doc.getElementsByTag("main").first();
//            Element section = main.getElementsByTag("section").first();
//            Elements ols = section.getElementsByClass("course-pack ember-view");
//
//            Element firstOl = ols.first();
//            Elements refers = firstOl.getElementsByTag("a");
//            for (Element link : refers) {
//                String linkHref = link.attr("href");
//                System.out.println(linkHref);
//            }
//
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
