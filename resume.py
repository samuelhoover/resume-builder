# pyright: basic

from resume_builder import (
    BoldText,
    Resume,
    Section,
    SectionEntry,
    ContactInfo,
    ConcatText,
    ItalicsText,
    UnderlinedText,
    LinkText,
    BulletedList,
)

resume = Resume(
    contact_info=ContactInfo(
        name="Samuel C. Hoover",
        details=[
            "samuel.charles.hoover@gmail.com",
            LinkText("samuelhoover.github.io", "https://samuelhoover.github.io"),
            LinkText(
                "linkedin.com/in/samuel-hoover",
                "https://www.linkedin.com/in/samuel-hoover/",
            ),
            LinkText("github.com/samuelhoover", "https://www.github.com/samuelhoover"),
        ],
        # tag_line="Making software as reliable as the sunrise.",
    ),
    sections=[
        Section(
            title="Experience",
            entries=[
                SectionEntry(
                    title=LinkText(
                        "Muthu Polymer Group", url="http://theory.pse.umass.edu"
                    ),
                    caption="Graduate Research Assistant",
                    location="UMass Amherst, Amherst, MA",
                    dates="Jan 2021 - Aug 2024",
                    description=BulletedList(
                        [
                            "Created a >260k row dataset and applied learning to predict conformations of sequence-defined polymers",
                            "Quantified effects of monomer sequence on self-assembly using SHAP values",
                            "Developed theory to model pH effects on polymer self-assemblies relevant to biological systems",
                            "Rewrote group legacy free energy minimization script to achieve 10x execution time speedup",
                        ]
                    ),
                ),
                SectionEntry(
                    title=LinkText(
                        "Triton Systems, Inc.", "https://www.tritonsystems.com"
                    ),
                    caption="Sensing & Separations Technologies Intern",
                    location="Chelmsford, MA",
                    dates="Jun 2023 - Sep 2023",
                    description=BulletedList(
                        [
                            "Designed induction heating coil to selectively desorb VOCs for ultra-low (< 1 ppm) molecular sensing device",
                            "Surveyed literature to recommend signal processing and data acquisition methods for breath VOCs analysis",
                        ],
                    ),
                ),
                SectionEntry(
                    title=LinkText(
                        "Bai Research Group", url="https://people.umass.edu/baigroup/"
                    ),
                    caption="Graduate Research Assistant",
                    location="UMass Amherst, Amherst, MA",
                    dates="Jan 2019 - Dec 2020",
                    description=BulletedList(
                        [
                            "Utilized convolutional neural networks for high-throughput virtual screening of nanoporous materials",
                            "Wrote deep learning pipeline using custom PyTorch modules to handle 3D volumetric data",
                            # "Computed force field parameters for organic small molecules using the Schr&ouml;dinger suite",
                        ]
                    ),
                ),
                SectionEntry(
                    title=LinkText("SI Group", "https://www.siigroup.com"),
                    caption="Global Manufacturing Technology Intern",
                    location="Schenectady, NY",
                    dates="May 2017 - Aug 2017",
                ),
            ],
        ),
        Section(
            title="Selected Presentations",
            entries=[
                SectionEntry(
                    title="UMass Amherst Chemical Engineering G.R.A.S.S. Talk",
                    description="Using machine learning to predict microphase separation transition of charged heteropolymers",
                    location="Amherst, MA",
                    dates="Oct 2023",
                ),
                # SectionEntry(
                #     title="Center for UMass / Industry Research on Polymers",
                #     description="Theory and quantitative assessment of pH-responsive polyzwitterion-polyelectrolyte complexation",
                #     location="Amherst, MA",
                #     dates="May 2023",
                # ),
                SectionEntry(
                    title="Nanopore Sequencing: From Genomes to Proteomes",
                    description="Computational design engine for accurate and efficient sequencing of DNA and RNA",
                    location="Boston, MA",
                    dates="Apr 2022",
                ),
            ],
        ),
        Section(
            title="Education",
            entries=[
                SectionEntry(
                    title="University of Massachusetts Amherst",
                    location="Amherst, MA",
                    dates="Sep 2018 - Aug 2024",
                    description=ConcatText(
                        ItalicsText("Ph.D. in Chemical Engineering"),
                        "<br>",
                        UnderlinedText("Thesis"),
                        ': "Study of Charged Macromolecule Phase Behavior using Conventional and Modern Modeling Methods"',
                        "<br>",
                        UnderlinedText("Awards"),
                        ": PPG Fellowship (Spring 2024), Teaching Assistant Award (Fall 2022)",
                    ),
                ),
                SectionEntry(
                    title="Clarkson University",
                    location="Potsdam, NY",
                    dates="Aug 2014 - May 2018",
                    description=ItalicsText(
                        "B.S. in Chemical Engineering; Minors in Mathematics and Cross-Cultural & International Perspectives",
                    ),
                ),
            ],
        ),
        Section(
            title="Skills",
            entries=[
                SectionEntry(
                    description=BulletedList(
                        [
                            ConcatText(
                                UnderlinedText("Languages"),
                                ": Python, C, Bash, MATLAB, HTML, LaTeX",
                            ),
                            ConcatText(
                                UnderlinedText("Tools"),
                                ": machine learning, polymer physics, molecular dynamics, PyTorch, scikit-learn, GROMACS, PyMOL, Git, AWS",
                            ),
                        ]
                    )
                ),
            ],
        ),
        Section(
            title="Publications & Ongoing Work",
            entries=[
                SectionEntry(
                    description=BulletedList(
                        [
                            ConcatText(
                                BoldText("Hoover, S. C."),
                                ", Li, S.-F. & Muthukumar, M. Learning the sequence effects on the microphase separation transition of charged heteropolymers. ",
                                BoldText("In preparation"),
                                ".",
                            ),
                            ConcatText(
                                BoldText("Hoover, S. C."),
                                ", Margossian, K. O. & Muthukumar, M. Theory and quantitative assessment of pH-responsive polyzwitterion-polyelectrolyte complexation. ",
                                ItalicsText("Soft Matter"),
                                " (2024) doi: ",
                                LinkText(
                                    "10.1039/D4SM00575A",
                                    url="https://doi.org/10.1039/D4SM00575A",
                                ),
                                ".",
                            ),
                            ConcatText(
                                "Liu, Y., Perez, G., Cheng, Z., Sun, A., ",
                                BoldText("Hoover, S. C."),
                                ", Fan, W., Maji, S., Bai, P. ZeoNet: 3D convolutional neural networks for predicting adsorption in nanoporous zeolites. ",
                                ItalicsText("J. Mater. Chem. A"),
                                BoldText(" 11"),
                                ", 17570-17580. (2023) doi: ",
                                LinkText(
                                    "10.1039/D3TA01911J",
                                    url="https://pubs.rsc.org/en/content/articlelanding/2023/ta/d3ta01911j",
                                ),
                                ".",
                            ),
                        ],
                    ),
                ),
            ],
        ),
    ],
)

if __name__ == "__main__":
    resume.cli_main()
