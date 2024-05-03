import "@typespec/versioning";
import "./providers/youtube.tsp";

using TypeSpec.Versioning;

@versioned(Versions)
@service({
    title: "vdl",
})
namespace Vdl;

enum Versions {
    v1,
}
