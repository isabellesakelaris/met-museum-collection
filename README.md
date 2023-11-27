# met-museum-collection
<p>Using The Met's <a href="https://github.com/metmuseum/openaccess">Open Access</a> data, this project looks at the differences between the Met's full open access dataset and the subset of works marked "Is Highlight." I would like to thank the museum for making their data publicly available. The version of the dataset that I downloaded was last updated in September of 2022, but I accessed it on March 10, 2023.</p>

<h2>General Collection Findings</h2>
<ul>
<li>As of March 10, 2023, there were 477,804 works in the dataset.</li>
<li>43.09% of thoe works are unattributed to a specific artist.</li>
<li>The artist with the most works in the dataset was Walker Evans, with 7,505 attributed works.</li>
<li>For works with a recorded Artist Nationality, 24.6% were by American Artists, which was the most commonly reported nationality.</li>
<li>For works with a recorded Culture, the most common values were American, then French, then Greek/Attic.</li>
<li>The department with the most works (in the dataset) was Drawings and Prints, with 167,152 works, or 34.98% of the entire dataset.</li>
<li>The most common Classification was "Prints."</li>
<li>The department with the least works was The Library, with 390 works, or 0.08% of the full dataset.</li>
</ul>

<h2>"Is Highlight" Collection</h2>
<ul>
<li>As of March 10, 2023, there were 2,484 works marked "Is Highlight" in the dataset.</li>
<li>27.81% of highlighted works were not attrubited to a known artist.</li>
<li>The artists with the most highlighted works—12 each—were Winslow Homer and John Singer Sargent.</li>
<li>391 out of 1,692 works with a recorded Artist Nationality were by American artists, which amounts to 23.1% of all highlighted works.</li>
<li>17.47% of highlighted works belong to The American Wing, but of all the works belonging to the department, only 2.36% of them were considered highlights.</li>
<li>The department with the highest share of highlighted works was The Library, which was made up of 96.41% highlighted works.</li>
<li>For works with a Classification, most were labeled paintings—262, or 14.64%. Only 49, or 2.74% were prints.</li>
</ul>

<h2>Findings</h2>
<ul>
<li>0.52% of all works in the dataset were considered highlights.</li>
<li>72% of highlighted works were attributed to a known artist vs. 57% overall, meaning The Met highlighted works by known artists at a higher rate than works by unkown artists. (Note: This makes sense to me, since the smaller share of highlighted works by unknown artists may be due to a lack of resources resulting from age or historic bias. However, since works by unknown artists make up over a quarter of all highlighted works, the museum seems to be making a concerted effort to showcase works by unknown artists anyway.) </li>
<li>14.64% of highlighted works were classified as paintings vs. 1.71% overall. Of those, most highlighted paintings were rendered in oil on canvas.</li>
<li>Though "Amnerican" was the most common artist nationality in both datasets, the share of works by American artists was smaller in the highlighted collection. That is, the museum did not favor works by American artists when designating an artwork as "is highlight," at least on the basis of artist nationality alone.</li>
<li>Based on the findings above, I hypothesize that The American Wing has the most highlighted works of any department because it houses more works by known artists than the general collection (64% vs. 57% overall) and more paintings rendered in oil on canvas than the general collection (5.28% vs. 0.72% overall).</li>
</ul>

<h2>Conclusion </h2>
<p>The Met's mission statement is as follows:<br /><br />"The Metropolitan Museum of Art collects, studies, conserves, and presents significant works of art across time and cultures in order to connect all people to creativity, knowledge, ideas, and one another."<br /><br />With such a large collection and comparatively limited exhibition space, museum staff must make decisions about which objects go "on view," under what conditions, and in what context. For example, when the European Paintings galleries reopened after a renovation in November 2023, some of the galleries were recurated, including gallery 639, which is now devoted to works "in process" such as <a href="https://www.metmuseum.org/art/collection/search/437819">my favorite Tinotretto</a>. In gallery 639, the museum staff have chosen to emphasize each artwork's unfinished state in order to teach the viewer about process. A more traditional approach might encourage the viewer to use the unfinsihed view of the work as a window into the artist's ideological or aesthetic vision and the way they work toward it instead. 
  
The art msuseum boards deem important enough to collect and preserve matters, as does the way musuem staff choose to display it. 


</p>


<h2>Assumptions</h2>
<ul>
<li>All works in the dataset are treated as equal—that is, since this dataset does not house data on every object in the Met's collection, it is likely that the musem has prioritized digitizing the metadata according to some internal criteria. For example, perhaps the metadata for the highlighted subset is complete but the general collections dataset is not. That would be relevant information!</li>
<li>Each department uses the same definitions for each field in the artwork metadata (even if they use different fields—for example, The American Wing does not have any works with a recorded artwork classification [painting, print, etc.]—the works belonging to this department only have a recorded medium [oil on canvas, charcoal on paper, etc.], which is more specific.)</li>
<li>Each department uses the same definition for "Is Highlight." I list this as an assumption because there is evidence that "Is Highlight" may be interpreted differently by distinct departments is the fact that the Library is made up of over 95% highlighted works, which is anomalous.</li>
</ul>

<h2>Acknowledgements</h2>
<p>Thank you to the Metropolitan Museum of Art for making these data publicly available.</p>
