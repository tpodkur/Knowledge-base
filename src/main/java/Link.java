
public class Link {
    private String link;
    private String section;

    public Link(String link, String section) {
        this.section = section;
        this.link = link;
    }

    public String getLink() { return link; }
    public String getSection() { return section; }
}
