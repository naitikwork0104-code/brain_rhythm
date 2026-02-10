from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/neural-clocks")
def neural_clocks():
    return render_template("neural_clocks.html")

@app.route("/human-study")
def human_study():
    return render_template("human_study.html")

@app.route("/quantum-computer")
def quantum_computer():
    return render_template("quantum_computer.html")

@app.route("/medical/cancer")
def cancer():
    return render_template("cancer.html")

@app.route("/medical/schizophrenia")
def schizophrenia():
    return render_template("schizophrenia.html")

@app.route("/medical/alzheimers")
def alzheimers():
    return render_template("alzheimers.html")

@app.route("/medical/thrombosis")
def thrombosis():
    return render_template("thrombosis.html")

@app.route("/proteins")
def protein():
    return render_template("protein.html")

@app.route("/proteins/circuit")
def circuit():
    return render_template("circuit.html")

@app.route("/proteins/vortex-synthesis")
def vortex_synthesis():
    return render_template("vortex_synthesis.html")

@app.route("/proteins/water")
def water():
    return render_template("water.html")

@app.route("/proteins/e-pi-phi")
def e_pi_phi():
    return render_template("e_pi_phi.html")

@app.route("/proteins/up-down-conversion")
def up_down_conversion():
    return render_template("up_down_conversion.html")

@app.route("/conference/matrisneha")
def matrisneha():
    return render_template("matrisneha.html")

@app.route("/conference/garima")
def garima():
    return render_template("garima.html")

@app.route("/conference/surobane")
def surobane():
    return render_template("surobane.html")

@app.route("/brain-components/cerebellum")
def cerebellum():
    return render_template("cerebellum.html")

@app.route("/brain-components/hippocampus")
def hippocampus():
    return render_template("hippocampus.html")

@app.route("/brain-components/blood-vessel-network")
def blood_vessel_network():
    return render_template("blood_vessel_network.html")

@app.route("/brain-components/hypothalamus")
def hypothalamus():
    return render_template("hypothalamus.html")

@app.route("/brain-components/microtubule")
def microtubule():
    return render_template("microtubule.html")

@app.route("/brain-components/cranial-nerve")
def cranial_nerve():
    return render_template("cranial_nerve.html")

@app.route("/brain-components/thalamic-body")
def thalamic_body():
    return render_template("thalamic_body.html")

@app.route("/brain-components/thoracic-nerve")
def thoracic_nerve():
    return render_template("thoracic_nerve.html")

@app.route("/brain-components/cortical-branches")
def cortical_branches():
    return render_template("cortical_branches.html")

@app.route("/brain-components/neuron")
def neuron():
    return render_template("neuron.html")

@app.route("/brain-components/skin-nerve-net")
def skin_nerve_net():
    return render_template("skin_nerve_net.html")

@app.route("/brain-components/cortex-domain")
def cortex_domain():
    return render_template("cortex_domain.html")

if __name__ == "__main__":
    app.run()

# gunicorn app:app --bind 0.0.0.0:8080 --workers 13 --threads 4
